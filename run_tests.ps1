# PowerShell script to run tests for EnginML package

Write-Host "Running tests for EnginML package" -ForegroundColor Cyan
Write-Host "=======================================" -ForegroundColor Cyan

Write-Host "`nInstalling test dependencies..." -ForegroundColor Yellow
python -m pip install -e ".[full]" pytest pytest-cov black isort

Write-Host "`nRunning unit tests..." -ForegroundColor Yellow
python -m pytest -v tests\test_core.py

Write-Host "`nRunning CLI tests..." -ForegroundColor Yellow
python -m pytest -v tests\test_cli.py

Write-Host "`nRunning integration tests..." -ForegroundColor Yellow
python -m pytest -v tests\test_integration.py

Write-Host "`nRunning end-to-end tests..." -ForegroundColor Yellow
python -m pytest -v tests\test_end_to_end.py

Write-Host "`nRunning all tests with coverage report..." -ForegroundColor Yellow
python -m pytest --cov=EnginML --cov-report=term-missing

Write-Host "`nAll tests completed!" -ForegroundColor Green
Write-Host "Check the test results above to verify the package works correctly." -ForegroundColor Green