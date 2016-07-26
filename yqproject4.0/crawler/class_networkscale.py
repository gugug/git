#coding=utf-8
__author__ = 'yc'
from crawler.class_save_data import *
from yqproject.settings import *

class NetworkScale(Database):
    def __init__(self):
        Database.__init__(self)

    # def get_sna(self,eid,ctime):
    #     """
    #     取sna图路径,用于前端network页展示用
    #     :param eid: event_id
    #     :param ctime: check_time
    #     :return: ({'sna_dir'},{},...) len=6
    #     """
    #     with self.conn:
    #         cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
    #         sql = "SELECT DISTINCT label_dir FROM networkscale WHERE event_id='%s' and check_time='%s'" % (eid, ctime)
    #         cur.execute(sql)
    #         rows = cur.fetchall()
    #         if len(rows) ==0:
    #             sql = "SELECT DISTINCT sna_dir FROM networkscale WHERE event_id='%s' ORDER BY check_time DESC limit 6" % eid
    #             cur.execute(sql)
    #             rows= cur.fetchall()
    #         if len(rows) == 0:
    #             default = BASE_DIR+'/network/result/SNA.png'
    #             return {'sna_dir':default}
    #         else :
    #             return rows

    def get_dirs(self,eid, ctime):
        """
        取label.xls路径,用于分析出网络图
        :param eid: event_id
        :param ctime: check_time
        :return:{'lable_dir':''}
        """
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            sql = "SELECT DISTINCT label_dir, sna_dir FROM networkscale WHERE event_id='%s' and check_time='%s'" % (eid, ctime)
            cur.execute(sql)
            rows = cur.fetchall()
            if len(rows) == 0:
                sql = "SELECT DISTINCT label_dir, sna_dir FROM networkscale WHERE event_id='%s' ORDER BY check_time DESC limit 1" % eid
                cur.execute(sql)
                rows = cur.fetchall()
            if len(rows) == 0:
                default_label ='/network/result/new_label_link.xls'
                default_sna = 'images/SNA.png'
                return {'label_dir':default_label,'sna_dir':default_sna}
            else:
                return rows[0]

    def get_leader(self,eid, ctime):
        """
        从network表中取出某时间点某事件的核心人物,暂时无用,保留
        """
        leader_list = []
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            sql = "SELECT DISTINCT leader FROM networkscale WHERE event_id='%s' and check_time='%s'" % (eid, ctime)
            cur.execute(sql)
            rows= cur.fetchall()
            if len(rows) == 0:
                return {'leader':'没有'}
            else :
                leader = rows[0]['leader'].split(',')
                leader_list.append(leader)
                return rows[0]
