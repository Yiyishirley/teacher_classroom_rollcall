# 把 Excel 读取库（SheetJS）合进 src.html，生成可离线使用的单文件「课堂点名.html」
# 用法：npm install && python3 build.py
from pathlib import Path

root = Path(__file__).parent
src = (root / "src.html").read_text(encoding="utf8")
lib = (root / "node_modules/xlsx/dist/xlsx.full.min.js").read_text(encoding="utf8").replace("</script", "<\\/script")
out = src.replace("<script>/*XLSX*/</script>", "<script>" + lib + "</script>", 1)
(root / "课堂点名.html").write_text(out, encoding="utf8")
print("已生成 课堂点名.html")
