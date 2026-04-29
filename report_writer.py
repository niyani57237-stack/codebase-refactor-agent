from pathlib import Path
from datetime import datetime


def write_markdown_report(
    analysis,
    quality_issues,
    refactor_suggestions,
    test_suggestions,
    output_path: Path,
):
    output_path.parent.mkdir(parents=True, exist_ok=True)

    summary = analysis["summary"]

    lines = []
    lines.append("# Codebase Analysis Report")
    lines.append("")
    lines.append(f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    lines.append("## 1. Project Summary")
    lines.append("")
    lines.append(f"- Files scanned: {summary['file_count']}")
    lines.append(f"- Total lines: {summary['total_lines']}")
    lines.append(f"- Functions found: {summary['function_count']}")
    lines.append(f"- Classes found: {summary['class_count']}")
    lines.append("")
    lines.append("## 2. File Structure Analysis")
    lines.append("")

    for file_info in analysis["files"]:
        lines.append(f"### {file_info['path']}")
        lines.append("")
        lines.append(f"- Line count: {file_info['line_count']}")
        lines.append(f"- Functions: {', '.join(file_info['functions']) if file_info['functions'] else 'None'}")
        lines.append(f"- Classes: {', '.join(file_info['classes']) if file_info['classes'] else 'None'}")
        lines.append(f"- Imports: {', '.join(file_info['imports']) if file_info['imports'] else 'None'}")
        lines.append(f"- Module docstring: {'Yes' if file_info['has_module_docstring'] else 'No'}")
        lines.append("")

    lines.append("## 3. Quality Issues")
    lines.append("")

    if quality_issues:
        for index, issue in enumerate(quality_issues, start=1):
            lines.append(f"{index}. **{issue['type']}** in `{issue['file']}`")
            lines.append(f"   - {issue['message']}")
    else:
        lines.append("No obvious quality issues detected.")
    lines.append("")

    lines.append("## 4. Refactoring Suggestions")
    lines.append("")

    for index, suggestion in enumerate(refactor_suggestions, start=1):
        lines.append(f"{index}. {suggestion}")
    lines.append("")

    lines.append("## 5. Unit Test Suggestions")
    lines.append("")

    for index, suggestion in enumerate(test_suggestions, start=1):
        lines.append(f"{index}. {suggestion}")
    lines.append("")

    lines.append("## 6. Multi-Agent Workflow Summary")
    lines.append("")
    lines.append(
        "The workflow follows a chain-style reasoning process: "
        "code scanning, structure parsing, quality diagnosis, refactoring planning, "
        "test planning and final report generation."
    )
    lines.append("")
    lines.append(
        "Each agent is responsible for one specific stage, and the Manager Agent "
        "coordinates the complete task pipeline."
    )
    lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")