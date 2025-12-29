-- Living Documentation Framework - Database Schema
-- SQLite 3.51.1+ Database Schema
--
-- Purpose: Rebuildable index for fast queries, graph analytics, and health monitoring
-- Source of Truth: Markdown files in Git
--
-- Created: 2025-12-29
-- Version: 1.0.0

-- Enable foreign keys
PRAGMA foreign_keys = ON;

-- Enable WAL mode for better concurrency
PRAGMA journal_mode = WAL;

-- ============================================================================
-- TABLE 1: documents (master table)
-- ============================================================================
CREATE TABLE IF NOT EXISTS documents (
    id TEXT PRIMARY KEY,                      -- Document ID (e.g., PRD-001-V2, ADR-005)
    file_path TEXT NOT NULL UNIQUE,           -- Relative path (engineering/requirements/prd.md)
    doc_type TEXT NOT NULL,                   -- Type (prd, tdd, adr, component, etc.)
    status TEXT NOT NULL,                     -- Status (draft, approved, deprecated)
    title TEXT NOT NULL,                      -- Document title
    domain TEXT,                              -- Domain/area
    created_at TEXT,                          -- Creation date (ISO 8601)
    updated_at TEXT,                          -- Last update date (ISO 8601)
    owner TEXT,                               -- Document owner
    content_hash TEXT,                        -- SHA256 hash for change detection
    metadata_json TEXT,                       -- Full YAML frontmatter (JSON)
    created_timestamp INTEGER DEFAULT (strftime('%s', 'now')),
    updated_timestamp INTEGER DEFAULT (strftime('%s', 'now'))
);

CREATE INDEX idx_documents_type ON documents(doc_type);
CREATE INDEX idx_documents_status ON documents(status);
CREATE INDEX idx_documents_owner ON documents(owner);
CREATE INDEX idx_documents_hash ON documents(content_hash);


-- ============================================================================
-- TABLE 2: living_doc_metadata (extended Living Documentation fields)
-- ============================================================================
CREATE TABLE IF NOT EXISTS living_doc_metadata (
    doc_id TEXT PRIMARY KEY REFERENCES documents(id) ON DELETE CASCADE,

    -- Semantic versioning
    version TEXT,                             -- "2.0.0"
    version_major INTEGER,
    version_minor INTEGER,
    version_patch INTEGER,

    -- Lifecycle tracking
    lifecycle_created TEXT,
    lifecycle_first_approved TEXT,
    lifecycle_last_modified TEXT,
    lifecycle_deprecated TEXT,
    lifecycle_sunset TEXT,

    -- Health status
    health_status TEXT,                       -- healthy, warning, critical
    health_last_check TEXT,
    health_checks_json TEXT,                  -- JSON array of health check results

    -- Deprecation
    is_deprecated BOOLEAN DEFAULT 0,
    superseded_by TEXT,                       -- Link to replacement document ID
    deprecation_reason TEXT,
    sunset_date TEXT,

    -- Additional metadata
    priority TEXT,                            -- low, medium, high, critical
    complexity TEXT,                          -- low, medium, high

    created_timestamp INTEGER DEFAULT (strftime('%s', 'now')),
    updated_timestamp INTEGER DEFAULT (strftime('%s', 'now'))
);

CREATE INDEX idx_living_metadata_health ON living_doc_metadata(health_status);
CREATE INDEX idx_living_metadata_deprecated ON living_doc_metadata(is_deprecated);
CREATE INDEX idx_living_metadata_version ON living_doc_metadata(version_major, version_minor, version_patch);


-- ============================================================================
-- TABLE 3: version_history (semantic versioning history)
-- ============================================================================
CREATE TABLE IF NOT EXISTS version_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doc_id TEXT NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    version TEXT NOT NULL,                    -- "2.1.0"
    version_date TEXT NOT NULL,               -- ISO 8601
    author TEXT,
    change_type TEXT,                         -- major, minor, patch
    summary TEXT,
    breaking BOOLEAN DEFAULT 0,               -- Is this a breaking change?
    changes_json TEXT,                        -- JSON array of specific changes
    impacts_json TEXT,                        -- JSON array of impacts
    created_timestamp INTEGER DEFAULT (strftime('%s', 'now'))
);

CREATE INDEX idx_version_history_doc ON version_history(doc_id);
CREATE INDEX idx_version_history_date ON version_history(version_date);
CREATE INDEX idx_version_history_breaking ON version_history(breaking);


-- ============================================================================
-- TABLE 4: edges (dependency graph)
-- ============================================================================
CREATE TABLE IF NOT EXISTS edges (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    from_id TEXT NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    to_id TEXT NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    edge_type TEXT NOT NULL,                  -- requires, informs, blocks, supersedes
    reason TEXT,                              -- Why this edge exists
    cascade BOOLEAN DEFAULT 0,                -- Should changes cascade?
    created_at TEXT DEFAULT (datetime('now')),
    updated_at TEXT DEFAULT (datetime('now')),
    UNIQUE(from_id, to_id, edge_type)
);

CREATE INDEX idx_edges_from ON edges(from_id);
CREATE INDEX idx_edges_to ON edges(to_id);
CREATE INDEX idx_edges_type ON edges(edge_type);


-- ============================================================================
-- TABLE 5: documents_fts (Full-Text Search via FTS5)
-- ============================================================================
CREATE VIRTUAL TABLE IF NOT EXISTS documents_fts USING fts5(
    id UNINDEXED,                             -- Document ID (not searchable)
    title,                                    -- Searchable title
    body,                                     -- Searchable body content
    content=''                                -- External content table
);

-- Triggers to keep FTS5 in sync with documents table
CREATE TRIGGER IF NOT EXISTS documents_fts_insert AFTER INSERT ON documents
BEGIN
    INSERT INTO documents_fts(rowid, id, title, body)
    VALUES (NEW.rowid, NEW.id, NEW.title, '');
END;

CREATE TRIGGER IF NOT EXISTS documents_fts_delete AFTER DELETE ON documents
BEGIN
    DELETE FROM documents_fts WHERE rowid = OLD.rowid;
END;

CREATE TRIGGER IF NOT EXISTS documents_fts_update AFTER UPDATE ON documents
BEGIN
    UPDATE documents_fts
    SET id = NEW.id, title = NEW.title
    WHERE rowid = NEW.rowid;
END;


-- ============================================================================
-- TABLE 6: health_checks (health check history)
-- ============================================================================
CREATE TABLE IF NOT EXISTS health_checks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doc_id TEXT NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    check_date TEXT NOT NULL DEFAULT (datetime('now')),
    overall_status TEXT NOT NULL,            -- healthy, warning, critical

    -- Individual check results
    freshness_status TEXT,
    freshness_details TEXT,

    dependency_status TEXT,
    dependency_details TEXT,

    cross_ref_status TEXT,
    cross_ref_details TEXT,

    owner_status TEXT,
    owner_details TEXT,

    sections_status TEXT,
    sections_details TEXT,

    upstream_status TEXT,
    upstream_details TEXT,

    satellite_status TEXT,
    satellite_details TEXT,

    created_timestamp INTEGER DEFAULT (strftime('%s', 'now'))
);

CREATE INDEX idx_health_checks_doc ON health_checks(doc_id);
CREATE INDEX idx_health_checks_date ON health_checks(check_date);
CREATE INDEX idx_health_checks_status ON health_checks(overall_status);


-- ============================================================================
-- TABLE 7: gaps (gap detection results)
-- ============================================================================
CREATE TABLE IF NOT EXISTS gaps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doc_id TEXT REFERENCES documents(id) ON DELETE CASCADE,
    gap_type TEXT NOT NULL,                  -- missing_dependency, broken_link, missing_section, etc.
    severity TEXT NOT NULL,                  -- low, medium, high, critical
    description TEXT NOT NULL,
    auto_fixable BOOLEAN DEFAULT 0,
    fix_suggestion TEXT,
    detected_at TEXT DEFAULT (datetime('now')),
    resolved_at TEXT,
    resolved_by TEXT,
    created_timestamp INTEGER DEFAULT (strftime('%s', 'now'))
);

CREATE INDEX idx_gaps_doc ON gaps(doc_id);
CREATE INDEX idx_gaps_type ON gaps(gap_type);
CREATE INDEX idx_gaps_severity ON gaps(severity);
CREATE INDEX idx_gaps_resolved ON gaps(resolved_at);


-- ============================================================================
-- TABLE 8: provenance (document lineage and audit trail)
-- ============================================================================
CREATE TABLE IF NOT EXISTS provenance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doc_id TEXT NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    action TEXT NOT NULL,                    -- created, updated, approved, deprecated
    actor TEXT,                              -- Who performed the action
    timestamp TEXT DEFAULT (datetime('now')),
    details TEXT,                            -- Additional context (JSON)
    git_commit TEXT,                         -- Git commit hash if available
    created_timestamp INTEGER DEFAULT (strftime('%s', 'now'))
);

CREATE INDEX idx_provenance_doc ON provenance(doc_id);
CREATE INDEX idx_provenance_action ON provenance(action);
CREATE INDEX idx_provenance_timestamp ON provenance(timestamp);


-- ============================================================================
-- TABLE 9: cross_reference_status (cross-reference validation)
-- ============================================================================
CREATE TABLE IF NOT EXISTS cross_reference_status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doc_id TEXT NOT NULL REFERENCES documents(id) ON DELETE CASCADE,

    -- Upstream changes
    upstream_pending_count INTEGER DEFAULT 0,
    upstream_high_severity_count INTEGER DEFAULT 0,
    upstream_acknowledged BOOLEAN DEFAULT 0,

    -- Downstream impacts
    downstream_pending_count INTEGER DEFAULT 0,
    downstream_notified BOOLEAN DEFAULT 0,

    last_check TEXT DEFAULT (datetime('now')),
    details_json TEXT,                       -- JSON details

    created_timestamp INTEGER DEFAULT (strftime('%s', 'now')),
    updated_timestamp INTEGER DEFAULT (strftime('%s', 'now'))
);

CREATE INDEX idx_cross_ref_doc ON cross_reference_status(doc_id);
CREATE INDEX idx_cross_ref_pending ON cross_reference_status(upstream_pending_count);


-- ============================================================================
-- TABLE 10: alternatives (decision alternatives and trade-offs)
-- ============================================================================
CREATE TABLE IF NOT EXISTS alternatives (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doc_id TEXT NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    alternative_name TEXT NOT NULL,
    description TEXT,
    pros TEXT,                               -- Pros (newline-separated or JSON)
    cons TEXT,                               -- Cons (newline-separated or JSON)
    decision TEXT,                           -- chosen, rejected, deferred
    rationale TEXT,
    created_timestamp INTEGER DEFAULT (strftime('%s', 'now'))
);

CREATE INDEX idx_alternatives_doc ON alternatives(doc_id);
CREATE INDEX idx_alternatives_decision ON alternatives(decision);


-- ============================================================================
-- TABLE 11: nodes (graph visualization metadata)
-- ============================================================================
CREATE TABLE IF NOT EXISTS nodes (
    id TEXT PRIMARY KEY REFERENCES documents(id) ON DELETE CASCADE,

    -- Visual properties
    x_position REAL,
    y_position REAL,
    color TEXT,
    shape TEXT,                              -- rectangle, ellipse, etc.
    size REAL,

    -- Graph metrics
    in_degree INTEGER DEFAULT 0,
    out_degree INTEGER DEFAULT 0,
    betweenness_centrality REAL,
    closeness_centrality REAL,
    pagerank REAL,

    -- Grouping
    cluster_id INTEGER,
    layer INTEGER,                           -- Hierarchical layer

    last_calculated TEXT DEFAULT (datetime('now')),
    created_timestamp INTEGER DEFAULT (strftime('%s', 'now')),
    updated_timestamp INTEGER DEFAULT (strftime('%s', 'now'))
);

CREATE INDEX idx_nodes_cluster ON nodes(cluster_id);
CREATE INDEX idx_nodes_layer ON nodes(layer);


-- ============================================================================
-- VIEWS for convenience
-- ============================================================================

-- View: Living Documentation documents with health status
CREATE VIEW IF NOT EXISTS vw_living_docs_health AS
SELECT
    d.id,
    d.title,
    d.doc_type,
    d.status,
    d.file_path,
    ldm.version,
    ldm.health_status,
    ldm.is_deprecated,
    ldm.superseded_by,
    d.owner,
    d.updated_at
FROM documents d
INNER JOIN living_doc_metadata ldm ON d.id = ldm.doc_id
ORDER BY d.id;


-- View: Dependency graph with document details
CREATE VIEW IF NOT EXISTS vw_dependency_graph AS
SELECT
    e.from_id,
    d1.title AS from_title,
    d1.doc_type AS from_type,
    e.edge_type,
    e.to_id,
    d2.title AS to_title,
    d2.doc_type AS to_type,
    e.cascade,
    e.reason
FROM edges e
INNER JOIN documents d1 ON e.from_id = d1.id
INNER JOIN documents d2 ON e.to_id = d2.id;


-- View: Recent health check summary
CREATE VIEW IF NOT EXISTS vw_health_summary AS
SELECT
    hc.doc_id,
    d.title,
    d.doc_type,
    hc.overall_status,
    hc.check_date,
    hc.freshness_status,
    hc.dependency_status,
    hc.cross_ref_status,
    hc.owner_status,
    hc.sections_status
FROM health_checks hc
INNER JOIN documents d ON hc.doc_id = d.id
WHERE hc.check_date = (
    SELECT MAX(check_date)
    FROM health_checks hc2
    WHERE hc2.doc_id = hc.doc_id
);


-- View: Unresolved gaps by severity
CREATE VIEW IF NOT EXISTS vw_unresolved_gaps AS
SELECT
    g.doc_id,
    d.title,
    d.doc_type,
    g.gap_type,
    g.severity,
    g.description,
    g.auto_fixable,
    g.fix_suggestion,
    g.detected_at
FROM gaps g
INNER JOIN documents d ON g.doc_id = d.id
WHERE g.resolved_at IS NULL
ORDER BY
    CASE g.severity
        WHEN 'critical' THEN 1
        WHEN 'high' THEN 2
        WHEN 'medium' THEN 3
        WHEN 'low' THEN 4
    END,
    g.detected_at DESC;


-- ============================================================================
-- TRIGGERS for automated timestamp updates
-- ============================================================================

CREATE TRIGGER IF NOT EXISTS trg_documents_update_timestamp
AFTER UPDATE ON documents
BEGIN
    UPDATE documents
    SET updated_timestamp = strftime('%s', 'now')
    WHERE id = NEW.id;
END;

CREATE TRIGGER IF NOT EXISTS trg_living_metadata_update_timestamp
AFTER UPDATE ON living_doc_metadata
BEGIN
    UPDATE living_doc_metadata
    SET updated_timestamp = strftime('%s', 'now')
    WHERE doc_id = NEW.doc_id;
END;

CREATE TRIGGER IF NOT EXISTS trg_nodes_update_timestamp
AFTER UPDATE ON nodes
BEGIN
    UPDATE nodes
    SET updated_timestamp = strftime('%s', 'now')
    WHERE id = NEW.id;
END;


-- ============================================================================
-- INITIALIZATION COMPLETE
-- ============================================================================

-- Verify schema
SELECT 'Schema created successfully - ' || COUNT(*) || ' tables' AS result
FROM sqlite_master
WHERE type = 'table' AND name NOT LIKE 'sqlite_%';
