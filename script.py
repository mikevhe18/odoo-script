#!/usr/bin/env python3
"""
Script Name: check_sequence_template.py
Author: SSI Development Team
Date: 2025-08-02
Description: Script untuk mengecek sequence template dengan pencarian field date yang dinamis

Usage:
    Script ini dirancang untuk dijalankan dalam Odoo Server Action.
    Variabel 'record' dan 'UserError' tersedia secara otomatis dalam konteks tersebut.

Dependencies:
    - Odoo environment (record, UserError)
    
Logic:
    1. Cari field dengan nama "date" terlebih dahulu
    2. Jika tidak ada, cari semua field dengan tipe Date
    3. Ambil field date pertama yang ditemukan
    4. Gunakan sebagai context untuk sequence generation
"""

# === MAIN SCRIPT LOGIC ===
# Note: Script ini berjalan dalam konteks Odoo Server Action
# Variabel 'record' dan 'UserError' sudah tersedia

result = ""
template = record._get_template_sequence()
ctx = {"ir_sequence_date": record.create_date}

if template:
    result = template.sequence_id.with_context(ctx).next_by_id()

# Output result untuk debugging/testing
raise UserError(result)
