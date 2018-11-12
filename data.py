import random

from flask import flash

page_ids = ['1-9', '1-10', '1-11', '1-12', '1-13', '1-14', '1-15', '1-16', '1-17', '1-18', '1-19', '1-20', '1-21', '1-22', '1-23', '1-24', '1-25', '1-26', '1-27', '1-28', '1-29', '1-30', '1-31', '1-32', '1-33', '1-34', '1-35', '1-36', '1-37', '1-38', '1-39', '1-40', '1-41', '1-42', '1-43', '1-44', '1-47', '1-48', '1-49', '1-50', '1-51', '1-52', '1-53', '1-54', '1-55', '1-56', '1-57', '1-58', '1-59', '1-60', '1-61', '1-62', '1-63', '1-64', '1-65', '1-66', '1-67', '1-68', '1-69', '1-70', '1-71', '1-72', '1-73', '1-74', '1-75', '1-76', '1-77', '1-78', '1-79', '1-80', '1-81', '1-82', '1-83', '1-84', '1-87', '1-88', '1-89', '1-90', '1-91', '1-92', '1-93', '1-94', '1-95', '1-96', '1-97', '1-98', '1-99', '1-100', '1-101', '1-102', '1-103', '1-104', '1-105', '1-106', '1-107', '1-108', '1-109', '1-110', '1-111', '1-112', '1-113', '1-114', '1-115', '1-116', '2-9', '2-10', '2-11', '2-12', '2-13', '2-14', '2-15', '2-16', '2-17', '2-18', '2-19', '2-20', '2-21', '2-22', '2-23', '2-24', '2-25', '2-26', '2-27', '2-28', '2-29', '2-30', '2-31', '2-32', '2-35', '2-36', '2-37', '2-38', '2-40', '2-41', '2-42', '2-43', '2-44', '2-45', '2-46', '2-47', '2-48', '2-49', '2-50', '2-51', '2-52', '2-53', '2-54', '2-55', '2-56', '2-57', '2-58', '2-61', '2-62', '2-63', '2-64', '2-65', '2-66', '2-67', '2-68', '2-69', '2-70', '2-71', '2-72', '2-73', '2-74', '2-75', '2-76', '2-77', '2-78', '2-79', '2-80', '2-81', '2-82', '2-83', '2-84', '2-85', '2-86', '2-87', '2-88', '2-89', '2-90', '2-93', '2-94', '2-95', '2-96', '2-97', '2-98', '2-99', '2-100', '2-101', '2-102', '2-103', '2-104', '2-105', '2-106', '2-107', '2-108', '2-109', '2-110', '2-111', '2-112', '2-113', '2-114', '2-115', '2-116', '3-9', '3-10', '3-11', '3-12', '3-13', '3-14', '3-15', '3-16', '3-17', '3-18', '3-19', '3-20', '3-21', '3-22', '3-23', '3-24', '3-25', '3-26', '3-27', '3-28', '3-29', '3-30', '3-31', '3-32', '3-35', '3-36', '3-37', '3-38', '3-39', '3-40', '3-41', '3-42', '3-43', '3-44', '3-45', '3-46', '3-47', '3-48', '3-49', '3-50', '3-51', '3-52', '3-53', '3-54', '3-55', '3-56', '3-57', '3-58', '3-61', '3-62', '3-63', '3-64', '3-65', '3-66', '3-67', '3-68', '3-69', '3-70', '3-71', '3-72', '3-73', '3-74', '3-75', '3-76', '3-77', '3-78', '3-79', '3-80', '3-81', '3-82', '3-83', '3-84', '3-85', '3-86', '3-87', '3-88', '3-89', '3-90', '3-91', '3-92', '3-94', '3-95', '3-96', '3-97', '3-98', '3-99', '3-100', '3-101', '3-103', '3-104', '3-105', '3-106', '3-107', '3-108', '3-109', '3-110', '3-111', '3-112', '3-113', '3-114', '3-115', '3-116', '4-9', '4-10', '4-11', '4-12', '4-13', '4-14', '4-15', '4-16', '4-17', '4-18', '4-19', '4-20', '4-21', '4-22', '4-23', '4-24', '4-25', '4-26', '4-27', '4-28', '4-29', '4-30', '4-31', '4-32', '4-33', '4-34', '4-35', '4-36', '4-37', '4-38', '4-39', '4-40', '4-42', '4-43', '4-44', '4-45', '4-46', '4-47', '4-48', '4-49', '4-51', '4-52', '4-53', '4-54', '4-55', '4-56', '4-57', '4-58', '4-59', '4-60', '4-61', '4-62', '4-63', '4-64', '4-65', '4-66', '4-67', '4-68', '4-69', '4-70', '4-71', '4-72', '4-73', '4-74', '4-76', '4-77', '4-78', '4-79', '4-80', '4-81', '4-82', '4-83', '4-85', '4-86', '4-87', '4-88', '4-89', '4-90', '4-91', '4-92', '4-93', '4-94', '4-95', '4-96', '4-97', '4-98', '4-99', '4-100', '4-101', '4-102', '4-103', '4-104', '4-105', '4-106', '4-107', '4-108', '4-109', '4-110', '4-111', '4-112', '4-113', '4-114', '4-115', '4-116', '5-9', '5-10', '5-11', '5-12', '5-13', '5-14', '5-15', '5-16', '5-17', '5-18', '5-19', '5-20', '5-21', '5-22', '5-23', '5-24', '5-25', '5-26', '5-27', '5-28', '5-29', '5-30', '5-31', '5-32', '5-35', '5-36', '5-37', '5-38', '5-39', '5-40', '5-41', '5-42', '5-43', '5-44', '5-45', '5-46', '5-47', '5-48', '5-49', '5-50', '5-51', '5-52', '5-53', '5-54', '5-55', '5-56', '5-57', '5-58', '5-59', '5-60', '5-61', '5-62', '5-63', '5-64', '5-65', '5-66', '5-67', '5-68', '5-69', '5-70', '5-71', '5-72', '5-73', '5-74', '5-77', '5-78', '5-79', '5-80', '5-81', '5-82', '5-83', '5-84', '5-85', '5-86', '5-87', '5-88', '5-89', '5-90', '5-91', '5-92', '5-93', '5-94', '5-95', '5-96', '5-97', '5-98', '5-99', '5-100', '5-101', '5-102', '5-103', '5-104', '5-105', '5-106', '5-107', '5-108', '5-109', '5-110', '5-111', '5-112', '5-113', '5-114', '5-115', '5-116', '6-9', '6-10', '6-11', '6-12', '6-13', '6-14', '6-15', '6-16', '6-17', '6-18', '6-19', '6-20', '6-21', '6-22', '6-23', '6-24', '6-25', '6-26', '6-27', '6-28', '6-29', '6-30', '6-31', '6-32', '6-33', '6-34', '6-35', '6-36', '6-37', '6-38', '6-39', '6-40', '6-41', '6-42', '6-43', '6-44', '6-45', '6-46', '6-49', '6-50', '6-51', '6-52', '6-53', '6-54', '6-55', '6-56', '6-57', '6-58', '6-59', '6-60', '6-61', '6-62', '6-63', '6-64', '6-67', '6-68', '6-69', '6-70', '6-71', '6-72', '6-73', '6-74', '6-75', '6-76', '6-77', '6-78', '6-79', '6-80', '6-81', '6-82', '6-83', '6-84', '6-85', '6-86', '6-87', '6-88', '6-89', '6-90', '6-92', '6-93', '6-94', '6-95', '6-96', '6-97', '6-98', '6-99', '6-100', '6-101', '6-102', '6-103', '6-104', '6-105', '6-106', '6-107', '6-109', '6-110', '6-111', '6-112', '6-113', '6-114', '6-115', '6-116', '7-9', '7-10', '7-11', '7-12', '7-13', '7-14', '7-15', '7-16', '7-17', '7-18', '7-19', '7-20', '7-21', '7-22', '7-23', '7-24', '7-25', '7-26', '7-27', '7-28', '7-29', '7-30', '7-33', '7-34', '7-35', '7-36', '7-37', '7-38', '7-39', '7-40', '7-41', '7-42', '7-43', '7-44', '7-45', '7-46', '7-47', '7-48', '7-51', '7-52', '7-53', '7-54', '7-55', '7-56', '7-57', '7-58', '7-59', '7-60', '7-61', '7-62', '7-63', '7-64', '7-65', '7-66', '7-69', '7-70', '7-71', '7-72', '7-73', '7-74', '7-75', '7-76', '7-77', '7-78', '7-79', '7-80', '7-81', '7-82', '7-83', '7-84', '7-86', '7-87', '7-88', '7-89', '7-90', '7-91', '7-92', '7-93', '7-94', '7-95', '7-96', '7-97', '7-98', '7-99', '7-101', '7-103', '7-104', '7-105', '7-106', '7-107', '7-108', '7-109', '7-110', '7-111', '7-112', '7-113', '7-114', '7-115', '7-116', '8-8', '8-9', '8-10', '8-11', '8-12', '8-13', '8-14', '8-15', '8-16', '8-17', '8-18', '8-19', '8-20', '8-21', '8-22', '8-23', '8-24', '8-25', '8-26', '8-27', '8-28', '8-29', '8-32', '8-33', '8-34', '8-35', '8-36', '8-37', '8-38', '8-39', '8-40', '8-41', '8-42', '8-43', '8-44', '8-45', '8-46', '8-47', '8-48', '8-49', '8-50', '8-51', '8-52', '8-53', '8-54', '8-55', '8-58', '8-59', '8-60', '8-61', '8-62', '8-63', '8-64', '8-65', '8-66', '8-67', '8-68', '8-69', '8-70', '8-71', '8-72', '8-73', '8-74', '8-75', '8-76', '8-77', '8-78', '8-79', '8-82', '8-83', '8-84', '8-85', '8-86', '8-87', '8-88', '8-89', '8-90', '8-91', '8-92', '8-93', '8-94', '8-95', '8-96', '8-98', '8-99', '8-100', '8-101', '8-102', '8-103', '8-104', '8-105', '8-106', '8-107', '8-108', '8-109', '8-112', '8-113', '8-114', '8-115', '9-9', '9-10', '9-11', '9-12', '9-13', '9-14', '9-15', '9-16', '9-17', '9-18', '9-19', '9-20', '9-21', '9-22', '9-23', '9-24', '9-25', '9-26', '9-27', '9-28', '9-29', '9-30', '9-33', '9-34', '9-35', '9-36', '9-37', '9-38', '9-39', '9-40', '9-41', '9-42', '9-43', '9-44', '9-45', '9-46', '9-47', '9-48', '9-49', '9-50', '9-51', '9-52', '9-53', '9-54', '9-55', '9-56', '9-59', '9-60', '9-61', '9-62', '9-63', '9-64', '9-66', '9-67', '9-68', '9-69', '9-70', '9-71', '9-72', '9-73', '9-74', '9-75', '9-76', '9-77', '9-78', '9-79', '9-80', '9-81', '9-82', '9-83', '9-84', '9-85', '9-86', '9-87', '9-88', '9-89', '9-90', '9-91', '9-92', '9-93', '9-94', '9-95', '9-97', '9-98', '9-99', '9-100', '9-101', '9-102', '9-103', '9-104', '9-105', '9-106', '9-107', '9-108', '9-109', '9-110', '9-111', '9-112', '9-113', '9-114', '9-115']


def get_image_data(db, koma_id):
    select_sql = """
    SELECT img_path, chara_num, whos, eyes, face_direction, step
    FROM yuyu_data WHERE koma_id = '{}'""".format(koma_id)
    cur = db.engine.execute(select_sql)
    data = cur.fetchone()
    return data


def get_page_data(db, page_id_idx):
    kanji, page = page_ids[page_id_idx].split('-')
    select_sql = """
    SELECT koma_id, kanji, page, img_path, chara_num, whos, eyes, face_direction
    FROM yuyu_data
    WHERE
        kanji = '{}' AND
        page = '{}'
    ORDER BY koma_id
    """.format(kanji, page)
    cur = db.engine.execute(select_sql)
    data = cur.fetchall()
    return data


def get_step1_inputer_dict(db):
    select_sql = 'SELECT step1_inputer, COUNT(step1_inputer) FROM yuyu_data GROUP BY step1_inputer'
    cur = db.engine.execute(select_sql)
    data = cur.fetchall()
    step1_inputer_dict = {name: count for name, count in data}
    return step1_inputer_dict


def fetch_next_rand_id(db):
    step1_ids_sql = 'SELECT koma_id FROM yuyu_data WHERE step = 1'
    step1_ids = db.engine.execute(step1_ids_sql).fetchall()

    if not step1_ids:
        return ''
    else:
        next_rand_id = random.choice(step1_ids)['koma_id']
        return next_rand_id


def update_step1(db, val_dict):
    update_sql = """
    UPDATE yuyu_data SET
    chara_num = {chara_num},
    whos = '{whos}',
    face_direction = '{face_direction}',
    eyes = '{eyes}',
    step1_inputer = '{step1_inputer}',
    step = 3
    where koma_id = '{koma_id}'
    """.format(**val_dict)

    db.engine.execute(update_sql)
    flash('update was successfully posted')


def get_graph_script(step1_inputer_dict):
    vals = list(step1_inputer_dict.values())
    vals.remove(max(vals))
    max_num = max(vals)
    display_max_num = (max_num // 100 + 2) * 100
    step1_inputer_dict['display_max_num'] = display_max_num

    graph_script = """
    <script type='text/javascript'>
      var data = {{
        labels: ['yuzuko({yuzuko})', 'yukari({yukari})', 'yui({yui})'],
        series: [{yuzuko},{yukari},{yui}]
      }};

      var options = {{
        distributeSeries: true,
        high: {display_max_num},
        showArea: true,
        showPoint: true,
        showLabel: true,

        labelInterpolationFnc: function(value) {{
        console.log(value)
            return value
        }}
      }}

      var chart = new Chartist.Bar('.ct-chart', data, options);
    </script>
    """.format(**step1_inputer_dict)
    return graph_script


def get_pie_chart_script(step1_inputer_dict):
    graph_script = """
    <script type='text/javascript'>
      var data = {{
        labels: ['yuzuko', 'yukari', 'yui', '未入力'],
        series: [{yuzuko},{yukari},{yui},{not_yet}]
      }};
      new Chartist.Pie('.ct-chart', data)

    </script>
    """.format(**step1_inputer_dict)
    return graph_script

# データを集めるカラム
# columns = ['koma_id', 'img_path', 'kanji', 'page', 'position', 'koma', 'size_x', 'size_y',
#            'chara_num', 'whos', 'eyes', 'face_direction',  # 1次入力
#            'place', 'background', 'serif_num', 'whos_s',  # 2次入力
#            'serifs', 'onomatope',  # 3次入力
#            'step', 'step1_inputer', 'step1_inputer', 'step3_inputer', ]  # 入力ステップ管理
