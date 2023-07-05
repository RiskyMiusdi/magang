# -*- coding: utf-8 -*-


from odoo import models, fields, api



#bagian daftar aset
from odoo import models, fields, api

class DaftarAset(models.Model):
  _name = 'tabel.aset'

  name              = fields.Char(readonly=False, store=True)
  # name              = fields.Boolean(string='Nam aset')
  # pasien = fields.Boolean(string='Pasien')
  # kode              = fields.Char(string='Kode', default='/')
  foto              = fields.Binary()
  nama_aset         = fields.Char(string="Nama Aset")
  lokasi         = fields.Char()
  merek             = fields.Char(string="Merek Aset")
  # jumlah            = fields.Float()
  harga_per_unit    = fields.Monetary(store=True, track_visibility='always')
  # harga_total       = fields.Monetary(compute="_compute_harga_total", store=True)
  # keterangan        = fields.Text()
  tanggal_beli      = fields.Date()
  currency_id       = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.user.company_id.currency_id)


  # @api.model
  # def create(self, vals):     
  #     if vals.get('name', False) and ('kode' not in vals or vals.get('kode', False) == '/'):
  #         vals['kode'] = self.env['ir.sequence'].get_sequence('Nama Aset Baru','tabel.aset','ASST')
  #     return super(DaftarAset, self).create(vals)

  @api.model
  def create(self, vals):
      if vals.get('name', 'New') == 'New':
          vals['name'] = self.env['ir.sequence'].next_by_code('tabel.aset') or 'Error!'
      return super(DaftarAset, self).create(vals)

  @api.depends('jumlah', 'harga_per_unit')
  def _compute_harga_total(self):
      for record in self:
          record.harga_total = record.jumlah * record.harga_per_unit

  @api.depends('harga_per_unit', 'jumlah')
  def _abc(self):
    self.harga_total = self.harga_per_unit * float(self.jumlah)

  # @api.multi
  # def cetak_aset(self):
  # return self.env['report'].get_action(self, 'manajemen_aset.laporan_aset')



#bagian member
class member(models.Model):      
  _inherit      = 'res.users'

  no_telepon    = fields.Char(string="No Telepon")
  ruang_kerja   = fields.Char(string="ruang kerja")
  hak_akses     = fields.Many2many('res.groups', 'res_groups_users_rel', 'uid', 'gid')
      
#bagian pengadaan aset
class pengadaan_aset(models.Model):
  _name = 'tabel.pengadaan.aset'

  name                  = fields.Char(string="Id Pengadaan")
  judul_pengadaan_aset  = fields.Char(string="Judul Pengadaan")      
  id_pengaju            = fields.Many2one('res.users', ondelete='cascade', string="ID Pengaju", required=True)                  
  merek                 = fields.Char(string="Merek")                
  tanggal_pengadaan     = fields.Date()
  jumlah                = fields.Float()
  # harga_per_unit      = fields.Integer()
  # harga_total         = fields.Float(compute="_xxx", store=True) 
  harga_per_unit        = fields.Monetary(store=True, track_visibility='always')  
  harga_total           = fields.Monetary(compute="_xxx", store=True)      
  currency_id       = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.user.company_id.currency_id)
  keterangan            = fields.Text(string="alasan pengadaan")
  state                 = fields.Selection([
                          ('draft', 'Draft'),
                          ('diajukan', 'Diajukan'),
                          ('disetujui', 'Disetujui'),
                          ], string='Status', readonly=True, copy=False, default='draft', track_visibility='onchange')

  @api.depends('harga_per_unit', 'jumlah' )
  def _xxx(self):
      self.harga_total = self.harga_per_unit * float(self.jumlah)

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
  merek                     = fields.Many2one('tabel.aset', ondelete='cascade', string="Merek", required=True)
  jumlah_pinjam             = fields.Integer()
  tanggal_peminjaman        = fields.Date()        
  keperluan                 = fields.Text()
  lokasi_penggunaan         = fields.Char(string="lokasi penggunaan")
  tanggal_kembali           = fields.Date()   
  id_peminjam               = fields.Many2one('res.users', ondelete='cascade', string="ID Peminjam", required=True)     
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
  merek                     = fields.Many2one('tabel.aset', ondelete='cascade', string="Merek", required=True)    
  jumlah_aset               = fields.Integer()
  kondisi_baik              = fields.Integer()
  kondisi_rusak             = fields.Integer()      
  kondisi_dalam_perbaikan   = fields.Integer()
  tanggal_inventaris        = fields.Date()
  petugas_inventaris        = fields.Many2one('res.users', ondelete='cascade', string="Petugas Inventaris", required=True)
  catatan                   = fields.Text()

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