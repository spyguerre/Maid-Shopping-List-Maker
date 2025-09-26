def get_excel_cell(i, j, lock_row=False, lock_col=False):
    """Convert Python indices (i, j) to Excel cell identifier (e.g., $A$1)."""
    def col_to_excel(col_idx):
        col_str = ""
        while col_idx >= 0:
            col_str = chr(col_idx % 26 + ord('A')) + col_str
            col_idx = col_idx // 26 - 1
        return col_str
    col = col_to_excel(j)
    row = str(i + 1)
    col_prefix = "$" if lock_col else ""
    row_prefix = "$" if lock_row else ""
    return f"{col_prefix}{col}{row_prefix}{row}"
