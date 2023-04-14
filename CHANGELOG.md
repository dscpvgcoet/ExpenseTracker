# Change Log

All notable changes to this project will be documented in this file.
 
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).
 
<!---
## [Unreleased] - yyyy-mm-dd

### ✨ Feature – for new features
### 🛠 Improvements – for general improvements
### 🚨 Changed – for changes in existing functionality
### ⚠️ Deprecated – for soon-to-be removed features
### 📚 Documentation – for documentation update
### 🗑 Removed – for removed features
### 🐛 Bug Fixes – for any bug fixes
### 🔒 Security – in case of vulnerabilities
### 🏗 Chore – for tidying code

See for sample https://raw.githubusercontent.com/favoloso/conventional-changelog-emoji/master/CHANGELOG.md
-->
## [1.2.0] - 2023-MM-DD
### 📚 Documentation
- Fix broken links to swagger and redoc ([#68](https://github.com/sebastienbarbier/seven23_server/issues/68))

## [1.1.0] - 2022-12-13
### ✨ Feature
- Allow **SQLite** for data storage ([#49](https://github.com/sebastienbarbier/seven23_server/issues/49))
### 🔒 Security
- Update dependencies ([#52](https://github.com/sebastienbarbier/seven23_server/issues/52))
### 🐛 Bug Fixes
- Fix broken password/reset/confirm API ([#60](https://github.com/sebastienbarbier/seven23_server/issues/60))
### 🏗 Chore
- Migrate **Continous Integration** from travis-ci to **Github actions** ([#40](https://github.com/sebastienbarbier/seven23_server/issues/40))
- Run within **Docker** ([#48](https://github.com/sebastienbarbier/seven23_server/issues/48))

## [1.0.1] - 2022-04-07
### 🔒 Security
- **Django** Security update ([#46](https://github.com/sebastienbarbier/seven23_server/issues/46))

## [1.0.0] - 2022-06-08
### ✨ Feature
- Initial **data model**
- **REST API** to fetch data models
- **Admin interface** for data handling.
- **Home page** with logo and redirection to [app.seven23.io](https://app.seven23.io)
### 📚 Documentation
- Implement **Swagger** and **redoc**.
- Export `docs` folder on **readthedocs**.