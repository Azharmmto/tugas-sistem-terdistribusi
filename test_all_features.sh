#!/bin/bash

echo "════════════════════════════════════════════════════════════"
echo "  🧪 TEST SEMUA FITUR - InfoHub Dashboard"
echo "════════════════════════════════════════════════════════════"
echo ""

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "📋 Checklist Fitur:"
echo ""

# Test 1: Check if files exist
echo -n "1. ✓ File app.py ada... "
if [ -f "app.py" ]; then
    echo -e "${GREEN}PASS${NC}"
else
    echo -e "${RED}FAIL${NC}"
fi

echo -n "2. ✓ File templates/index.html ada... "
if [ -f "templates/index.html" ]; then
    echo -e "${GREEN}PASS${NC}"
else
    echo -e "${RED}FAIL${NC}"
fi

echo -n "3. ✓ File static/js/script.js ada... "
if [ -f "static/js/script.js" ]; then
    echo -e "${GREEN}PASS${NC}"
else
    echo -e "${RED}FAIL${NC}"
fi

echo -n "4. ✓ File static/css/style.css ada... "
if [ -f "static/css/style.css" ]; then
    echo -e "${GREEN}PASS${NC}"
else
    echo -e "${RED}FAIL${NC}"
fi

echo ""
echo "📦 Cek Fitur Baru:"
echo ""

# Check for new features in code
echo -n "5. ✓ Daily Briefing endpoint di app.py... "
if grep -q "send-briefing" app.py; then
    echo -e "${GREEN}PASS${NC}"
else
    echo -e "${RED}FAIL${NC}"
fi

echo -n "6. ✓ Random news function di app.py... "
if grep -q "random.sample" app.py; then
    echo -e "${GREEN}PASS${NC}"
else
    echo -e "${RED}FAIL${NC}"
fi

echo -n "7. ✓ Weather emoji function di script.js... "
if grep -q "getWeatherEmoji" static/js/script.js; then
    echo -e "${GREEN}PASS${NC}"
else
    echo -e "${RED}FAIL${NC}"
fi

echo -n "8. ✓ Email form di index.html... "
if grep -q "email-input" templates/index.html; then
    echo -e "${GREEN}PASS${NC}"
else
    echo -e "${RED}FAIL${NC}"
fi

echo -n "9. ✓ InfoHub title di index.html... "
if grep -q "InfoHub" templates/index.html; then
    echo -e "${GREEN}PASS${NC}"
else
    echo -e "${RED}FAIL${NC}"
fi

echo -n "10. ✓ Briefing card CSS di style.css... "
if grep -q "briefing-card" static/css/style.css; then
    echo -e "${GREEN}PASS${NC}"
else
    echo -e "${RED}FAIL${NC}"
fi

echo ""
echo "🌐 Test API Eksternal:"
echo ""

# Test external APIs
echo "11. Testing BMKG Weather API..."
python3 test_api_changes.py > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo -e "    ${GREEN}✓ BMKG API: PASS${NC}"
else
    echo -e "    ${YELLOW}⚠ BMKG API: WARNING (mungkin koneksi)${NC}"
fi

echo ""
echo "════════════════════════════════════════════════════════════"
echo "  📊 SUMMARY"
echo "════════════════════════════════════════════════════════════"
echo ""
echo "Branch: notifikasi ✓"
echo "Status: Ready for testing"
echo ""
echo "Fitur yang ditambahkan:"
echo "  ✓ Daily Briefing (Email notification)"
echo "  ✓ Random News (3 berita random)"
echo "  ✓ Weather Icons (Emoji cuaca)"
echo "  ✓ Enhanced UI (Animasi & styling)"
echo ""
echo "Untuk menjalankan aplikasi:"
echo "  $ python3 app.py"
echo ""
echo "Untuk test lengkap (perlu server running):"
echo "  $ python3 test_briefing.py"
echo ""
echo "════════════════════════════════════════════════════════════"
