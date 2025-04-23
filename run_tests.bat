@echo off
echo Running tests for EnginML package
echo =======================================

echo Installing test dependencies...
pip install -e ".[full]" pytest pytest-cov black isort

echo.
echo Running unit tests...
pytest -v tests\test_core.py

echo.
echo Running CLI tests...
pytest -v tests\test_cli.py

echo.
echo Running integration tests...
pytest -v tests\test_integration.py

echo.
echo Running end-to-end tests...
pytest -v tests\test_end_to_end.py

echo.
echo Running all tests with coverage report...
pytest --cov=EnginML --cov-report=term-missing

echo.
echo All tests completed!
echo Check the test results above to verify the package works correctly.