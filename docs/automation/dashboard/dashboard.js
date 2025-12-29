/**
 * Living Documentation Dashboard - Main JavaScript
 *
 * Loads health check data, impact graph, deprecation warnings, and recent changes
 * Auto-refreshes every 15 minutes
 */

// Configuration
const CONFIG = {
    refreshInterval: 15 * 60 * 1000, // 15 minutes in milliseconds
    healthCheckDataUrl: '../reports/health-report.json',
    impactDataUrl: '../reports/impact-report.json',
    deprecationDataUrl: '../reports/deprecation-report.json',
    recentChangesDataUrl: '../reports/recent-changes.json'
};

// Global state
let healthChart = null;
let impactGraph = null;
let refreshTimer = null;

/**
 * Initialize dashboard on page load
 */
document.addEventListener('DOMContentLoaded', () => {
    loadDashboard();
    setupAutoRefresh();
    setupEventListeners();
});

/**
 * Main function to load all dashboard data
 */
async function loadDashboard() {
    updateLastUpdateTime();

    try {
        await Promise.all([
            loadHealthSummary(),
            loadDeprecationWarnings(),
            loadRecentChanges(),
            loadHealthIssues()
        ]);

        // Impact graph loads separately (slower)
        loadImpactGraph();
    } catch (error) {
        console.error('Error loading dashboard:', error);
        showError('Failed to load dashboard data');
    }
}

/**
 * Load health summary data and render stats + chart
 */
async function loadHealthSummary() {
    try {
        const data = await fetchJSON(CONFIG.healthCheckDataUrl);

        if (!data) {
            useMockHealthData();
            return;
        }

        // Update stat cards
        const healthyCnt = data.documents?.filter(d => d.health_status === 'healthy').length || 0;
        const warningCnt = data.documents?.filter(d => d.health_status === 'warning').length || 0;
        const criticalCnt = data.documents?.filter(d => d.health_status === 'critical').length || 0;
        const totalCnt = data.documents?.length || 0;

        document.getElementById('healthy-count').textContent = healthyCnt;
        document.getElementById('warning-count').textContent = warningCnt;
        document.getElementById('critical-count').textContent = criticalCnt;
        document.getElementById('total-count').textContent = totalCnt;

        // Render health score chart
        renderHealthChart(healthyCnt, warningCnt, criticalCnt);

    } catch (error) {
        console.error('Error loading health summary:', error);
        useMockHealthData();
    }
}

/**
 * Use mock data for demonstration when real data unavailable
 */
function useMockHealthData() {
    console.log('Using mock health data');

    document.getElementById('healthy-count').textContent = '42';
    document.getElementById('warning-count').textContent = '8';
    document.getElementById('critical-count').textContent = '3';
    document.getElementById('total-count').textContent = '53';

    renderHealthChart(42, 8, 3);
}

/**
 * Render health score chart using Chart.js
 */
function renderHealthChart(healthy, warning, critical) {
    const ctx = document.getElementById('healthScoreChart');

    // Destroy existing chart if any
    if (healthChart) {
        healthChart.destroy();
    }

    healthChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Healthy', 'Warnings', 'Critical'],
            datasets: [{
                data: [healthy, warning, critical],
                backgroundColor: [
                    'rgb(16, 185, 129)', // green
                    'rgb(245, 158, 11)', // orange
                    'rgb(239, 68, 68)'   // red
                ],
                borderWidth: 2,
                borderColor: '#fff'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        padding: 20,
                        font: {
                            size: 14
                        }
                    }
                },
                title: {
                    display: true,
                    text: 'Document Health Distribution',
                    font: {
                        size: 16,
                        weight: 'bold'
                    },
                    padding: 20
                }
            }
        }
    });
}

/**
 * Load and render deprecation warnings
 */
async function loadDeprecationWarnings() {
    const container = document.getElementById('deprecation-warnings');

    try {
        const data = await fetchJSON(CONFIG.deprecationDataUrl);

        if (!data || !data.warnings || data.warnings.length === 0) {
            container.innerHTML = '<div class="empty-state"><div class="empty-state-icon">✅</div><p>No deprecation warnings</p></div>';
            return;
        }

        container.innerHTML = data.warnings.map(warning => `
            <div class="warning-item ${warning.status}">
                <div class="warning-item-header">
                    <div class="warning-item-title">📄 ${warning.document_id}</div>
                    <span class="warning-badge ${warning.status}">${warning.status}</span>
                </div>
                <div class="warning-item-detail">${warning.warning}</div>
                ${warning.sunset_date ? `<div class="warning-item-detail"><strong>Sunset:</strong> ${warning.sunset_date}</div>` : ''}
                ${warning.migration_target ? `<div class="warning-item-detail"><strong>Migration target:</strong> ${warning.migration_target}</div>` : ''}
            </div>
        `).join('');

    } catch (error) {
        console.error('Error loading deprecation warnings:', error);
        container.innerHTML = '<div class="empty-state"><div class="empty-state-icon">✅</div><p>No deprecation warnings</p></div>';
    }
}

/**
 * Load and render impact graph using vis.js
 */
async function loadImpactGraph() {
    try {
        const data = await fetchJSON(CONFIG.impactDataUrl);

        if (!data) {
            useMockImpactGraph();
            return;
        }

        renderImpactGraph(data);

    } catch (error) {
        console.error('Error loading impact graph:', error);
        useMockImpactGraph();
    }
}

/**
 * Use mock impact graph for demonstration
 */
function useMockImpactGraph() {
    console.log('Using mock impact graph');

    const mockData = {
        nodes: [
            { id: 'VISION', label: 'VISION', group: 'pre-production', level: 0 },
            { id: 'PRD', label: 'PRD', group: 'engineering', level: 1 },
            { id: 'TDD', label: 'TDD', group: 'engineering', level: 1 },
            { id: 'ADR-001', label: 'ADR-001', group: 'engineering', level: 2 },
            { id: 'ADR-002', label: 'ADR-002', group: 'engineering', level: 2 },
            { id: 'IMPL-PLAN', label: 'IMPL-PLAN', group: 'implementation', level: 3 }
        ],
        edges: [
            { from: 'VISION', to: 'PRD' },
            { from: 'PRD', to: 'TDD' },
            { from: 'PRD', to: 'ADR-001' },
            { from: 'TDD', to: 'ADR-002' },
            { from: 'ADR-001', to: 'IMPL-PLAN' },
            { from: 'ADR-002', to: 'IMPL-PLAN' }
        ]
    };

    renderImpactGraph(mockData);
}

/**
 * Render impact graph using vis.js
 */
function renderImpactGraph(data) {
    const container = document.getElementById('impact-graph');

    // Destroy existing network if any
    if (impactGraph) {
        impactGraph.destroy();
    }

    // Define node groups with colors
    const groups = {
        'pre-production': { color: { background: '#dbeafe', border: '#2563eb' } },
        'engineering': { color: { background: '#fef3c7', border: '#f59e0b' } },
        'implementation': { color: { background: '#d1fae5', border: '#10b981' } },
        'operations': { color: { background: '#e0e7ff', border: '#6366f1' } },
        'deprecated': { color: { background: '#fee2e2', border: '#ef4444' } }
    };

    // Create vis.js network
    const nodes = new vis.DataSet(data.nodes || []);
    const edges = new vis.DataSet(data.edges || []);

    const networkData = {
        nodes: nodes,
        edges: edges
    };

    const options = {
        nodes: {
            shape: 'box',
            margin: 10,
            widthConstraint: {
                maximum: 150
            },
            font: {
                size: 14,
                face: 'Arial'
            }
        },
        edges: {
            arrows: {
                to: {
                    enabled: true,
                    scaleFactor: 0.5
                }
            },
            smooth: {
                type: 'cubicBezier',
                forceDirection: 'vertical',
                roundness: 0.4
            }
        },
        layout: {
            hierarchical: {
                enabled: true,
                direction: 'UD',
                sortMethod: 'directed',
                levelSeparation: 150,
                nodeSpacing: 100
            }
        },
        groups: groups,
        physics: {
            enabled: false
        },
        interaction: {
            hover: true,
            tooltipDelay: 200
        }
    };

    impactGraph = new vis.Network(container, networkData, options);

    // Event listeners for graph controls
    document.getElementById('show-deprecated').addEventListener('change', (e) => {
        const show = e.target.checked;
        nodes.forEach(node => {
            if (node.group === 'deprecated') {
                nodes.update({ id: node.id, hidden: !show });
            }
        });
    });

    document.getElementById('show-satellites').addEventListener('change', (e) => {
        const show = e.target.checked;
        nodes.forEach(node => {
            if (node.group === 'satellite') {
                nodes.update({ id: node.id, hidden: !show });
            }
        });
    });
}

/**
 * Load and render recent changes
 */
async function loadRecentChanges() {
    const container = document.getElementById('recent-changes');

    try {
        const data = await fetchJSON(CONFIG.recentChangesDataUrl);

        if (!data || !data.changes || data.changes.length === 0) {
            useMockRecentChanges(container);
            return;
        }

        renderRecentChanges(container, data.changes);

    } catch (error) {
        console.error('Error loading recent changes:', error);
        useMockRecentChanges(container);
    }
}

/**
 * Use mock recent changes for demonstration
 */
function useMockRecentChanges(container) {
    console.log('Using mock recent changes');

    const mockChanges = [
        {
            document_id: 'DOC-PRD-003',
            change_type: 'modified',
            version: '2.1.0',
            timestamp: new Date(Date.now() - 2 * 60 * 60 * 1000).toISOString(),
            author: 'Developer'
        },
        {
            document_id: 'DOC-ADR-012',
            change_type: 'new',
            version: '1.0.0',
            timestamp: new Date(Date.now() - 5 * 60 * 60 * 1000).toISOString(),
            author: 'Architect'
        },
        {
            document_id: 'DOC-TDD-008',
            change_type: 'modified',
            version: '1.5.0',
            timestamp: new Date(Date.now() - 8 * 60 * 60 * 1000).toISOString(),
            author: 'QA Engineer'
        }
    ];

    renderRecentChanges(container, mockChanges);
}

/**
 * Render recent changes list
 */
function renderRecentChanges(container, changes) {
    container.innerHTML = changes.map(change => `
        <div class="change-item ${change.change_type}">
            <span class="change-badge ${change.change_type}">${change.change_type}</span>
            <div class="change-info">
                <div class="change-title">${change.document_id}</div>
                <div class="change-meta">v${change.version} • ${change.author || 'Unknown'}</div>
            </div>
            <div class="change-timestamp">${formatRelativeTime(change.timestamp)}</div>
        </div>
    `).join('');
}

/**
 * Load and render health issues
 */
async function loadHealthIssues() {
    const container = document.getElementById('health-issues');

    try {
        const data = await fetchJSON(CONFIG.healthCheckDataUrl);

        if (!data || !data.documents) {
            useMockHealthIssues(container);
            return;
        }

        // Extract documents with issues
        const issues = data.documents.filter(doc =>
            doc.health_status === 'warning' || doc.health_status === 'critical'
        );

        if (issues.length === 0) {
            container.innerHTML = '<div class="empty-state"><div class="empty-state-icon">✅</div><p>No health issues found</p></div>';
            return;
        }

        renderHealthIssues(container, issues);

    } catch (error) {
        console.error('Error loading health issues:', error);
        useMockHealthIssues(container);
    }
}

/**
 * Use mock health issues for demonstration
 */
function useMockHealthIssues(container) {
    console.log('Using mock health issues');

    const mockIssues = [
        {
            document_id: 'DOC-PRD-001',
            health_status: 'warning',
            failed_checks: ['freshness'],
            issues: ['Document not modified in 45 days']
        },
        {
            document_id: 'DOC-ADR-003',
            health_status: 'critical',
            failed_checks: ['dependencies', 'cross-references'],
            issues: ['Missing dependency: DOC-PRD-999', 'Broken cross-reference to DOC-TDD-005']
        },
        {
            document_id: 'DOC-TDD-002',
            health_status: 'warning',
            failed_checks: ['owner'],
            issues: ['No owner assigned']
        }
    ];

    renderHealthIssues(container, mockIssues);
}

/**
 * Render health issues list
 */
function renderHealthIssues(container, issues) {
    container.innerHTML = issues.map(issue => `
        <div class="issue-item ${issue.health_status}">
            <div class="issue-header">
                <div class="issue-title">📄 ${issue.document_id}</div>
                <span class="issue-badge ${issue.health_status}">${issue.health_status}</span>
            </div>
            <div class="issue-description">
                ${(issue.issues || []).map(i => `• ${i}`).join('<br>')}
            </div>
            <div class="issue-checks">
                ${(issue.failed_checks || []).map(check =>
                    `<span class="issue-check failed">❌ ${check}</span>`
                ).join('')}
            </div>
        </div>
    `).join('');
}

/**
 * Setup filter buttons for health issues
 */
function setupEventListeners() {
    const filterBtns = document.querySelectorAll('.filter-btn');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Update active state
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            // Filter issues
            const filter = btn.dataset.filter;
            filterHealthIssues(filter);
        });
    });
}

/**
 * Filter health issues by type
 */
function filterHealthIssues(filter) {
    const issues = document.querySelectorAll('.issue-item');

    issues.forEach(issue => {
        if (filter === 'all') {
            issue.style.display = '';
        } else {
            const checks = issue.querySelectorAll('.issue-check');
            let hasFilter = false;

            checks.forEach(check => {
                if (check.textContent.includes(filter)) {
                    hasFilter = true;
                }
            });

            issue.style.display = hasFilter ? '' : 'none';
        }
    });
}

/**
 * Setup auto-refresh timer
 */
function setupAutoRefresh() {
    // Clear existing timer
    if (refreshTimer) {
        clearInterval(refreshTimer);
    }

    // Set new timer
    refreshTimer = setInterval(() => {
        console.log('Auto-refreshing dashboard...');
        loadDashboard();
    }, CONFIG.refreshInterval);

    console.log(`Auto-refresh enabled: every ${CONFIG.refreshInterval / 1000 / 60} minutes`);
}

/**
 * Update last update time display
 */
function updateLastUpdateTime() {
    const now = new Date();
    const timeString = now.toLocaleTimeString('pl-PL', {
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
    });
    document.getElementById('last-update').textContent = `Last update: ${timeString}`;
}

/**
 * Fetch JSON data from URL with error handling
 */
async function fetchJSON(url) {
    try {
        const response = await fetch(url);

        if (!response.ok) {
            console.warn(`Failed to fetch ${url}: ${response.status}`);
            return null;
        }

        return await response.json();
    } catch (error) {
        console.warn(`Error fetching ${url}:`, error.message);
        return null;
    }
}

/**
 * Format timestamp as relative time
 */
function formatRelativeTime(timestamp) {
    const now = new Date();
    const date = new Date(timestamp);
    const diffMs = now - date;
    const diffMins = Math.floor(diffMs / 60000);
    const diffHours = Math.floor(diffMs / 3600000);
    const diffDays = Math.floor(diffMs / 86400000);

    if (diffMins < 1) return 'Just now';
    if (diffMins < 60) return `${diffMins}m ago`;
    if (diffHours < 24) return `${diffHours}h ago`;
    return `${diffDays}d ago`;
}

/**
 * Show error message to user
 */
function showError(message) {
    console.error(message);
    // Could add toast notification here
}
