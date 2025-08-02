#!/usr/bin/env python3
result = ""
template = record._get_template_sequence()

# Cari field date yang sesuai
date_field_value = None

# 1. Prioritas pertama: cari field dengan nama "date"
if hasattr(record, 'date') and record.date:
    date_field_value = record.date
else:
    # 2. Jika tidak ada field "date", cari field dengan tipe Date
    date_fields = []
    for field_name, field_obj in record._fields.items():
        if field_obj.type == 'date' and getattr(record, field_name, None):
            date_fields.append((field_name, getattr(record, field_name)))
    
    # Ambil data pertama jika ditemukan lebih dari satu
    if date_fields:
        date_field_value = date_fields[0][1]

raise UserError(date_field_value or getattr(record, 'date_voucher', None))
# Gunakan date_field_value atau fallback ke date_voucher jika tersedia
ctx = {"ir_sequence_date": date_field_value or getattr(record, 'date_voucher', None)}

if template:
    result = template.sequence_id.with_context(ctx).next_by_id()

# Output result untuk debugging/testing
raise UserError(result)
