import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from mcp import Client  # noqa: E402
from mcp_server import server, wiki_read  # noqa: E402


class MCPServerTests(unittest.IsolatedAsyncioTestCase):
    async def test_protocol_lists_and_calls_tools(self) -> None:
        async with Client(server) as client:
            tools = await client.list_tools()
            self.assertEqual(
                {tool.name for tool in tools.tools},
                {"wiki_search", "wiki_ingest", "wiki_lint", "wiki_read", "wiki_stats"},
            )

            result = await client.call_tool("wiki_stats", {})
            stats = json.loads(result.content[0].text)
            self.assertGreater(stats["total_pages"], 4_000)
            self.assertIn("strategy", stats["by_type"])

    async def test_wiki_read_allows_wiki_markdown(self) -> None:
        content = await wiki_read("wiki/index.md")
        self.assertIn("AlgoBrain", content)

    async def test_wiki_read_blocks_path_traversal(self) -> None:
        for path in ("README.md", "../README.md", str(ROOT / "README.md")):
            with self.subTest(path=path):
                result = await wiki_read(path)
                self.assertTrue(result.startswith("Invalid page path:"))


if __name__ == "__main__":
    unittest.main()
