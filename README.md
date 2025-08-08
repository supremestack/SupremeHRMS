# Supreme HRMS

Enterprise Human Resource Management System for Odoo 16+

## Overview

Supreme HRMS is a comprehensive HR management solution built on Odoo Community Edition, leveraging OCA modules for maximum functionality with minimal custom code.

**Developer**: Supreme Stack Systems Limited  
**Website**: [www.supremestack.net](https://www.supremestack.net)  
**Domain**: supremestack.net

## Features

✅ **Employee Management**
- Comprehensive employee records
- Auto-generated employee IDs
- Emergency contacts
- Banking information
- Document management

✅ **Attendance & Time Tracking**
- GPS-based attendance
- Work from home support
- Shift management
- Overtime calculation

✅ **Leave Management**
- Multiple leave types
- Half-day leave support
- Leave balance tracking
- Team calendar view

✅ **Payroll Processing**
- Multi-country payroll
- Automated tax calculations
- Loan management
- Bank file generation

✅ **Self-Service Portal**
- Employee dashboard
- Leave applications
- Expense submissions
- Document access

✅ **REST API**
- Mobile app integration
- Third-party integrations
- OAuth2 authentication

## Architecture

```
supreme-hrms/
├── supreme_core/        # Core HR extensions
├── supreme_dashboard/   # Analytics dashboard
├── supreme_api/        # REST API endpoints
└── docs/              # Documentation
```

## Dependencies

### Odoo CE Modules (Built-in)
- hr
- hr_attendance
- hr_holidays
- hr_expense
- hr_recruitment
- hr_contract
- hr_skills

### OCA Modules (Forked)
- [supremestack/hr](https://github.com/supremestack/hr)
- [supremestack/payroll](https://github.com/supremestack/payroll)
- [supremestack/server-tools](https://github.com/supremestack/server-tools)
- [supremestack/rest-framework](https://github.com/supremestack/rest-framework)
- [supremestack/web](https://github.com/supremestack/web)

## Installation

### Quick Install

```bash
# 1. Clone repository
git clone -b 18.0 https://github.com/supremestack/supreme-hrms.git

# 2. Copy to Odoo addons
cp -r supreme-hrms/* /opt/odoo/addons/

# 3. Install OCA dependencies
cd /opt/odoo/
git clone -b 18.0 https://github.com/supremestack/hr.git oca-hr
git clone -b 18.0 https://github.com/supremestack/payroll.git oca-payroll

# 4. Update Odoo config
# Add to addons_path in odoo.conf

# 5. Restart Odoo
sudo service odoo restart

# 6. Update Apps List and Install
```

### Detailed Installation

See [INSTALL.md](INSTALL.md) for complete installation guide.

## Version Compatibility

| Odoo Version | Branch | Status |
|-------------|---------|---------|
| 18.0 | 18.0 | ✅ Stable |
| 17.0 | 17.0 | ✅ Stable |
| 16.0 | 16.0 | ✅ Stable |

## Configuration

1. **Company Setup**
   - Settings → Companies
   - Configure company information

2. **HR Settings**
   - Settings → Human Resources
   - Enable required features

3. **Employee Data**
   - Import existing employee data
   - Configure departments
   - Set up leave types

4. **API Access**
   - Settings → Technical → API Keys
   - Generate keys for mobile apps

## API Documentation

### Authentication
```bash
curl -X POST https://your-domain/api/auth/token \
  -H "Content-Type: application/json" \
  -d '{"api_key": "your_api_key"}'
```

### Endpoints
- `POST /api/attendance/checkin` - Clock in
- `POST /api/attendance/checkout` - Clock out
- `GET /api/leave/balance` - Get leave balance
- `POST /api/leave/request` - Submit leave request
- `GET /api/employee/profile` - Get employee profile

See [API.md](docs/API.md) for complete API documentation.

## Development

### Setup Development Environment

```bash
# Clone with submodules
git clone --recursive https://github.com/supremestack/supreme-hrms.git

# Install pre-commit hooks
pip install pre-commit
pre-commit install

# Run tests
python -m pytest
```

### Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Run tests
5. Submit pull request

### Code Standards

- Follow OCA guidelines
- PEP 8 compliance
- 100% test coverage for new code
- Documentation required

## Support

- 📧 Email: support@supremestack.net
- 🐛 Issues: [GitHub Issues](https://github.com/supremestack/supreme-hrms/issues)
- 📖 Wiki: [Documentation](https://github.com/supremestack/supreme-hrms/wiki)

## License

LGPL-3.0 - See [LICENSE](LICENSE) file

## Credits

Developed by **Supreme Stack Systems Limited**

Contributors:
- Supreme Stack Development Team
- Odoo Community Association (OCA)

---

© 2024 Supreme Stack Systems Limited. All rights reserved.
