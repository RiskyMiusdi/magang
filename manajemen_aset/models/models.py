# -*- coding: utf-8 -*-

from odoo import models, fields, api

#bagian daftar aset
class daftar_aset(models.Model):
      _name = 'tabel.aset'    

      name = fields.Char(string="ID Aset")      
      nama_aset         = fields.Char(string="Nama Aset")      
      merek             = fields.Char(string="Merek Aset")
      jumlah            = fields.Float()
      harga_per_unit    = fields.Integer()
      harga_total       = fields.Float(compute="_value_pc", store=True)      
      keterangan        = fields.Text()
      foto              = fields.Binary() 

      @api.depends('harga_per_unit', 'jumlah' )
      def _value_pc(self):
          self.harga_total = float(self.harga_per_unit) * self.jumlah

      @api.multi
      def cetak_aset(self):
        return self.env['report'].get_action(self, 'manajemen_aset.laporan_aset')



#bagian member
class member(models.Model):      
      _inherit = 'res.users'

                  
      no_telepon        = fields.Char(string="No Telepon")
      ruang_kerja       = fields.Char(string="ruang kerja")
      hak_akses = fields.Many2many('res.groups', 'res_groups_users_rel', 'uid', 'gid')
      
      
   

#bagian pengadaan aset
class pengadaan_aset(models.Model):
      _name = 'tabel.pengadaan.aset'

      name                  = fields.Char(string="Id Pengadaan")
      judul_pengadaan_aset  = fields.Char(string="Judul Pengadaan")      
      merek                 = fields.Char(string="Merek Aset")
      jumlah                = fields.Integer()
      harga_per_unit        = fields.Integer()
      harga_total           = fields.Integer()      
      tanggal_pengadaan     = fields.Date()    
      nama_pengaju          = fields.Char(string="nama pengaju")
      id_pengaju            = fields.Char(string="id pengaju")            
      keterangan            = fields.Text(string="alasan pengadaan")
      state = fields.Selection([
        ('draft', 'Draft'),
        ('diajukan', 'Diajukan'),
        ('disetujui', 'Disetujui'),
        ], string='Status', readonly=True, copy=False, default='draft', track_visibility='onchange')

      @api.multi
      def cetak_pengadaan(self):
        return self.env['report'].get_action(self, 'manajemen_aset.laporan_pengadaan')

      @api.multi
      def action_confirm(self):
          self.write({'state': 'diajukan'})

      @api.multi
      def action_cancel(self):
          self.write({'state': 'draft'})

      @api.multi
      def action_close(self):
          self.write({'state': 'disetujui'})  

#bagian peminjaman aset
class peminjaman_aset(models.Model):
      _name = 'tabel.peminjaman.aset'

      name                      = fields.Char(string="Id Peminjaman")
      judul_peminjaman          = fields.Char(string="Judul Peminjaman")      
      merek                     = fields.Char(string="Merek Aset")
      jumlah_pinjam             = fields.Integer()
      tanggal_peminjaman        = fields.Date()
      kode_peminjaman           = fields.Char(string="kode peminjaman")
      keperluan                 = fields.Text()
      lokasi_penggunaan         = fields.Char(string="lokasi penggunaan")
      tanggal_kembali           = fields.Date()   
      nama_peminjam             = fields.Char(string="nama peminjam")

      state = fields.Selection([
        ('draft', 'Draft'),
        ('diajukan', 'Diajukan'),
        ('disetujui', 'Disetujui'),
        ], string='Status', readonly=True, copy=False, default='draft', track_visibility='onchange')

      @api.multi
      def cetak_peminjaman(self):
        return self.env['report'].get_action(self, 'manajemen_aset.laporan_peminjaman')

      @api.multi
      def action_confirm(self):
          self.write({'state': 'diajukan'})

      @api.multi
      def action_cancel(self):
          self.write({'state': 'draft'})

      @api.multi
      def action_close(self):
          self.write({'state': 'disetujui'})         



#bagian inventaris aset
class inventarisasi_aset(models.Model):
      _name = 'tabel.inventaris.aset'

      name                      = fields.Char(string="Id Inventaris")
      judul_inventaris          = fields.Char(string="Judul Inventaris")      
      # ?id_inventaris             = fields.Char(string="id inventaris")
      merek                     = fields.Char(string="Merek Aset")
      jumlah_aset               = fields.Integer()
      kondisi_baik              = fields.Integer()
      kondisi_rusak             = fields.Integer()      
      kondisi_dalam_perbaikan   = fields.Integer()
      tanggal_inventaris        = fields.Date()
      tanggal_dimusnahkan       = fields.Date()   
      lokasi_aset               = fields.Char(string="lokasi terkini")
      harga_per_unit            = fields.Char(string="harga per unit")
      harga_total_aset          = fields.Char(string="harga total aset")
      tanggal_pengadaan         = fields.Date()
      kode_pengadaan            = fields.Char(string="kode pengadaan")
      status_pengadaan          = fields.Char(string="status pengadaan")
      nama_pengaju              = fields.Char(string="nama pengaju")
      id_pengaju                = fields.Char(string="id pengaju")
      petugas_aproval           = fields.Char(string="petugas aproval")
      id_petugas                = fields.Char(string="id petugas")
      keterangan                = fields.Char(string="keterangan")
      kode_inventaris           = fields.Char(string="kode inventaris")
      petugas_inventaris        = fields.Char(string="petugas inventaris")

      state = fields.Selection([
        ('draft', 'Draft'),
        ('diajukan', 'Diajukan'),
        ('disetujui', 'Disetujui'),
        ], string='Status', readonly=True, copy=False, default='draft', track_visibility='onchange')

      @api.multi
      def cetak_inventaris(self):
        return self.env['report'].get_action(self, 'manajemen_aset.laporan_inventaris')

      @api.multi
      def action_confirm(self):
          self.write({'state': 'diajukan'})

      @api.multi
      def action_cancel(self):
          self.write({'state': 'draft'})

      @api.multi
      def action_close(self):
          self.write({'state': 'disetujui'})   