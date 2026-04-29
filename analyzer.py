import ast
from pathlib import Path


def analyze_codebase(files):
    file_reports = []
    total_functions = 0
    total_classes = 0
    total_lines = 0

    for file_path in files:
        try:
            source = Path(file_path).read_text(encoding="utf-8")
        except UnicodeDecodeError:
            source = Path(file_path).read_text(encoding="gbk", errors="ignore")

        lines = source.splitlines()
        total_lines += len(lines)

        try:
            tree = ast.parse(source)
        except SyntaxError:
            file_reports.append(
                {
                    "path": str(file_path),
                    "line_count": len(lines),
                    "functions": [],
                    "classes": [],
                    "imports": [],
                    "has_module_docstring": False,
                    "function_details": [],
                    "syntax_error": True,
                }
            )
            continue

        functions = []
        classes = []
        imports = []
        function_details = []

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                functions.append(node.name)

                function_length = 0
                if hasattr(node, "end_lineno") and node.end_lineno:
                    function_length = node.end_lineno - node.lineno + 1

                function_details.append(
                    {
                        "name": node.name,
                        "line": node.lineno,
                        "length": function_length,
                        "has_docstring": ast.get_docstring(node) is not None,
                    }
                )

            elif isinstance(node, ast.ClassDef):
                classes.append(node.name)

            elif isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(alias.name)

            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.append(node.module)

        total_functions += len(functions)
        total_classes += len(classes)

        file_reports.append(
            {
                "path": str(file_path),
                "line_count": len(lines),
                "functions": functions,
                "classes": classes,
                "imports": sorted(set(imports)),
                "has_module_docstring": ast.get_docstring(tree) is not None,
                "function_details": function_details,
                "syntax_error": False,
            }
        )

    return {
        "summary": {
            "file_count": len(files),
            "function_count": total_functions,
            "class_count": total_classes,
            "total_lines": total_lines,
        },
        "files": file_reports,
    }


def detect_quality_issues(analysis):
    issues = []

    for file_info in analysis["files"]:
        path = file_info["path"]

        if file_info.get("syntax_error"):
            issues.append(
                {
                    "file": path,
                    "type": "Syntax Error",
                    "message": "This file has a syntax error and cannot be parsed by AST.",
                }
            )
            continue

        if file_info["line_count"] > 200:
            issues.append(
                {
                    "file": path,
                    "type": "Large File",
                    "message": "This file has more than 200 lines. Consider splitting it into smaller modules.",
                }
            )

        if not file_info["has_module_docstring"]:
            issues.append(
                {
                    "file": path,
                    "type": "Missing Module Docstring",
                    "message": "This file does not contain a module-level docstring.",
                }
            )

        for func in file_info["function_details"]:
            if func["length"] > 40:
                issues.append(
                    {
                        "file": path,
                        "type": "Long Function",
                        "message": f"Function `{func['name']}` is {func['length']} lines long. Consider refactoring it.",
                    }
                )

            if not func["has_docstring"]:
                issues.append(
                    {
                        "file": path,
                        "type": "Missing Function Docstring",
                        "message": f"Function `{func['name']}` does not contain a docstring.",
                    }
                )

    return issues