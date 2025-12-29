---
id: CONTINGENCY-001
title: "Contingency Plan: Parser Failure"
type: contingency-plan
risk_id: RISK-TBD (Parser Implementation Risk)
component: COMP-001-parser
sprint: Sprint 1
status: active
date: "2025-12-28"
---

# Contingency Plan: Parser Failure

## Trigger Conditions
Activate this plan if ANY of:
1. **Critical Bug**: python-frontmatter crashes on >10% real docs (unrecoverable)
2. **Performance**: Parse time >10s dla 100 docs (2x target, unfixable)
3. **Maintenance**: python-frontmatter abandoned (no updates 12+ months, critical CVE)
4. **Licensing**: python-frontmatter license change (incompatible z our use case)

## Detection
- **Sprint 1 Week 1**: Test python-frontmatter on 100 real docs z `/engineering/`
- **Metrics**: Track parse success rate, performance, exceptions
- **Threshold**: If success rate <90% or perf >10s → TRIGGER contingency

## Plan B: Switch to PyYAML + Regex

### Approach
Replace python-frontmatter z custom implementation:
1. Use `PyYAML` dla frontmatter parsing
2. Use `regex` dla frontmatter boundary detection (`---`)
3. Use `markdown-it-py` dla content parsing (unchanged)

### Implementation Effort
- **Coding**: 2 days (rewrite parser.py, ~300 LOC)
- **Testing**: 1 day (update test fixtures, regression tests)
- **Total**: 3 days

### Code Example
```python
import re
import yaml

def parse_frontmatter_custom(content: str) -> tuple[dict, str]:
    """Custom frontmatter parser (fallback dla python-frontmatter)"""
    # Match YAML frontmatter block (--- ... ---)
    pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(pattern, content, re.DOTALL)

    if not match:
        return {}, content  # No frontmatter

    frontmatter_raw = match.group(1)
    markdown_content = match.group(2)

    try:
        frontmatter = yaml.safe_load(frontmatter_raw)
    except yaml.YAMLError as e:
        raise ParseError(f"Invalid YAML: {e}")

    return frontmatter, markdown_content
```

### Risks of Plan B
- ✅ Low risk: PyYAML widely used, stable
- ✅ Similar API to python-frontmatter (easy swap)
- ❌ Custom code = maintenance burden (but <500 LOC)

## Plan C: Switch to mistletoe

### Approach
Use `mistletoe` (pure Python markdown parser z frontmatter support).

### Pros/Cons
- ✅ All-in-one (frontmatter + markdown parsing)
- ❌ Less popular (900 GitHub stars vs python-frontmatter 1.2k)
- ❌ Performance unknown (no benchmark)

### Effort
- 4 days (less similar API, more rewrite)

**Verdict**: Plan C = last resort if Plan B also fails.

## Decision Tree
```
python-frontmatter fails?
    ├─ YES → Is failure fixable w 1 week?
    │         ├─ YES → Fix + continue
    │         └─ NO → Trigger Plan B (PyYAML+regex)
    │                   └─ Plan B implementation takes >5 days?
    │                       ├─ NO → Proceed (acceptable delay)
    │                       └─ YES → Escalate to Product Owner
    │                                 └─ Consider Plan C or delay Sprint 1
    └─ NO → Continue with python-frontmatter
```

## Communication Plan
If contingency triggered:
1. **Immediate**: Notify Product Owner + Tech Lead (Slack + email)
2. **Day 1**: Document failure mode (create evidence note E-XXX)
3. **Day 2**: Start Plan B implementation
4. **Day 5**: Plan B complete, regression tests pass
5. **Day 6**: Update ADR-006 (document pivot decision)

## Success Criteria (Plan B)
- [ ] Parse success rate ≥95% (same as original target)
- [ ] Performance <5s dla 100 docs (NFR-001 met)
- [ ] All tests pass (100% coverage maintained)
- [ ] 0 critical bugs introduced

## Sign-Off
- **Plan Author**: Tech Lead
- **Reviewed By**: Product Owner, QA Lead
- **Approved**: YES / NO
- **Date**: 2025-12-28
