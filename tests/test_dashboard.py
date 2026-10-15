import json
import re
from pathlib import Path
import sys
import tempfile
import unittest
import pandas as pd
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from dashboard import build_dashboard, make_dashboard


class DashboardTests(unittest.TestCase):
    def test_notebook_sources_do_not_embed_cloud_credentials(self):
        pattern = re.compile(r'''["'](?:apikey|access_key_id|secret_access_key)["']\s*:\s*["'][A-Za-z0-9/+_=-]{16,}["']''')
        for path in Path(__file__).resolve().parents[1].glob('*.ipynb'):
            notebook = json.loads(path.read_text())
            for cell in notebook['cells']:
                self.assertIsNone(pattern.search(''.join(cell.get('source', []))))

    def test_dates_are_joined_instead_of_positionally_paired(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pd.DataFrame({'date': [2001, 2000], 'change-current': [2, 1]}).to_csv(root/'gdp.csv', index=False)
            pd.DataFrame({'date': [2000, 2001], 'unemployment': [4, 3]}).to_csv(root/'jobs.csv', index=False)
            plot = build_dashboard(root/'gdp.csv', root/'jobs.csv', root/'dashboard.html')
            source = plot.renderers[1].data_source.data
            self.assertEqual(list(source['x']), [2000, 2001])
            self.assertEqual(list(source['y']), [4, 3])
            self.assertIn('US economic indicators', (root/'dashboard.html').read_text())

    def test_mismatched_series_are_rejected(self):
        with self.assertRaises(ValueError):
            make_dashboard([2000], [1, 2], [3], 'Test', 'unused.html')

    def test_notebooks_have_valid_schema_and_no_saved_outputs(self):
        import nbformat
        for path in Path(__file__).resolve().parents[1].glob('*.ipynb'):
            notebook = nbformat.read(path, as_version=4)
            nbformat.validate(notebook)
            for cell in notebook.cells:
                if cell.cell_type == 'code':
                    self.assertEqual(cell.outputs, [])
                    self.assertIsNone(cell.execution_count)
                    compile(cell.source, str(path), 'exec')


if __name__ == '__main__':
    unittest.main()
