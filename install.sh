#!/bin/bash
#
# Supreme HRMS Installation Script
# For Odoo 16.0, 17.0, and 18.0
#

set -e

echo "========================================"
echo "Supreme HRMS Installation Script"
echo "========================================"

# Configuration
ODOO_VERSION=${1:-18.0}
ODOO_PATH="/opt/odoo"
ADDONS_PATH="$ODOO_PATH/addons"
OCA_PATH="$ODOO_PATH/oca"

echo "Installing for Odoo $ODOO_VERSION"

# Create directories
echo "Creating directories..."
sudo mkdir -p $OCA_PATH
sudo chown -R $USER:$USER $OCA_PATH

# Clone Supreme HRMS
echo "Cloning Supreme HRMS..."
cd $ADDONS_PATH
git clone -b $ODOO_VERSION https://github.com/supremestack/supreme-hrms.git

# Clone OCA dependencies
echo "Cloning OCA dependencies..."
cd $OCA_PATH

# Essential OCA modules
git clone -b $ODOO_VERSION https://github.com/supremestack/hr.git
git clone -b $ODOO_VERSION https://github.com/supremestack/payroll.git
git clone -b $ODOO_VERSION https://github.com/supremestack/server-tools.git
git clone -b $ODOO_VERSION https://github.com/supremestack/rest-framework.git
git clone -b $ODOO_VERSION https://github.com/supremestack/web.git

# Optional OCA modules
git clone -b $ODOO_VERSION https://github.com/supremestack/dms.git || true
git clone -b $ODOO_VERSION https://github.com/supremestack/reporting-engine.git || true

# Update Odoo configuration
echo "Updating Odoo configuration..."
ODOO_CONF="/etc/odoo/odoo.conf"

if [ -f "$ODOO_CONF" ]; then
    echo "Backing up existing configuration..."
    sudo cp $ODOO_CONF "$ODOO_CONF.backup"
    
    # Update addons_path
    echo "Updating addons_path..."
    # This is simplified - in production, properly parse and update the config
    echo "Please manually update addons_path in $ODOO_CONF to include:"
    echo "  $ADDONS_PATH/supreme-hrms"
    echo "  $OCA_PATH/hr"
    echo "  $OCA_PATH/payroll"
    echo "  $OCA_PATH/server-tools"
    echo "  $OCA_PATH/rest-framework"
    echo "  $OCA_PATH/web"
fi

# Install Python dependencies
echo "Installing Python dependencies..."
pip3 install --user \
    psycopg2-binary \
    Pillow \
    lxml \
    python-dateutil \
    pytz \
    reportlab \
    xlrd \
    xlwt \
    openpyxl

echo "========================================"
echo "Installation completed!"
echo "========================================"
echo ""
echo "Next steps:"
echo "1. Update addons_path in $ODOO_CONF"
echo "2. Restart Odoo service: sudo systemctl restart odoo"
echo "3. Update Apps List in Odoo"
echo "4. Install Supreme HRMS modules"
echo ""
echo "Modules to install in order:"
echo "  1. Supreme HRMS Core"
echo "  2. Supreme HRMS Dashboard"
echo "  3. Supreme HRMS API"
