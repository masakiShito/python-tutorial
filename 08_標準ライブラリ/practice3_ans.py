# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

def datetime_module_practice():
    # 現在の日付を取得
    now = datetime.now()
    formatted_now = now.strftime('%Y-%m-%d')
    print(f"現在の日付: {formatted_now}")

    # 1ヶ月後の日付を取得
    one_month_later = now + timedelta(days=30)
    formatted_one_month_later = one_month_later.strftime('%Y-%m-%d')
    print(f"1ヶ月後の日付: {formatted_one_month_later}")

datetime_module_practice()
