#! /usr/bin/env python
#coding=utf-8

from snapshot_selenium import snapshot as driver
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.render import make_snapshot

def pie_chart() -> Pie:
    pie = Pie()
    attr = ['失败', '中断', '通过', '跳过', '未知']
    value = [12, 22, 34, 29, 16]
    c = (
        pie.add("", [list(z) for z in zip(attr, value)]).set_global_opts(
            title_opts=opts.TitleOpts(title="成功率统计")).set_series_opts(
            label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c

# 需要安装 snapshot_selenium
make_snapshot(driver, pie_chart().render(), "pie.png")
