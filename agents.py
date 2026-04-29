from pathlib import Path
from analyzer import analyze_codebase, detect_quality_issues
from report_writer import write_markdown_report


class ScannerAgent:
    def run(self, target_path: Path):
        print("[Scanner Agent] Scanning target codebase...")
        files = list(target_path.rglob("*.py"))
        return files


class StructureAgent:
    def run(self, files):
        print("[Structure Agent] Parsing code structure...")
        return analyze_codebase(files)


class QualityAgent:
    def run(self, analysis):
        print("[Quality Agent] Detecting code quality issues...")
        return detect_quality_issues(analysis)


class RefactorAgent:
    def run(self, analysis, quality_issues):
        print("[Refactor Agent] Generating refactoring suggestions...")

        suggestions = []

        if analysis["summary"]["function_count"] > 0:
            suggestions.append("Split long functions into smaller single-responsibility functions.")

        if analysis["summary"]["class_count"] == 0:
            suggestions.append("Consider introducing classes or modules to organize related logic.")

        if quality_issues:
            suggestions.append("Prioritize files with long functions, missing docstrings, or high line counts.")

        suggestions.append("Move repeated logic into reusable helper functions.")
        suggestions.append("Add clearer naming for variables, functions and modules.")

        return suggestions


class TestAgent:
    def run(self, analysis):
        print("[Test Agent] Generating unit test suggestions...")

        suggestions = []

        for file_info in analysis["files"]:
            for function_name in file_info["functions"]:
                suggestions.append(
                    f"Add unit tests for function `{function_name}` in `{file_info['path']}`."
                )

        if not suggestions:
            suggestions.append("No functions detected. Add tests after implementing core logic.")

        return suggestions


class ReportAgent:
    def run(
        self,
        analysis,
        quality_issues,
        refactor_suggestions,
        test_suggestions,
        output_path: Path,
    ):
        print("[Report Agent] Writing Markdown report...")

        write_markdown_report(
            analysis=analysis,
            quality_issues=quality_issues,
            refactor_suggestions=refactor_suggestions,
            test_suggestions=test_suggestions,
            output_path=output_path,
        )

        return output_path


class ManagerAgent:
    def __init__(self, target_path: Path, output_path: Path):
        self.target_path = target_path
        self.output_path = output_path

    def run(self):
        print("[Manager Agent] Starting multi-agent workflow...")

        scanner = ScannerAgent()
        structure = StructureAgent()
        quality = QualityAgent()
        refactor = RefactorAgent()
        test = TestAgent()
        report = ReportAgent()

        files = scanner.run(self.target_path)
        analysis = structure.run(files)
        quality_issues = quality.run(analysis)
        refactor_suggestions = refactor.run(analysis, quality_issues)
        test_suggestions = test.run(analysis)
        report_path = report.run(
            analysis,
            quality_issues,
            refactor_suggestions,
            test_suggestions,
            self.output_path,
        )

        print("[Manager Agent] Task completed.")

        return {
            "summary": analysis["summary"],
            "quality_issues": quality_issues,
            "refactor_suggestions": refactor_suggestions,
            "test_suggestions": test_suggestions,
            "report_path": report_path,
        }