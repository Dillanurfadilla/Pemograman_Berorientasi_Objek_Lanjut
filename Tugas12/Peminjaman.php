<?php
//Simpanlah dengan nama file : Peminjaman.php
require_once 'database.php';
class Peminjaman 
{
    private $db;
    private $table = 'peminjaman';
    public $nomor_bukti = "";
    public $kode_anggota = "";
    public $tanggal_pinjam = "";
    public $tanggal_kembali = "";
    public $kode_buku = "";
    public function __construct(MySQLDatabase $db)
    {
        $this->db = $db;
    }
    public function get_all() 
    {
        $query = "SELECT * FROM $this->table";
        $result_set = $this->db->query($query);
        return $result_set;
    }
    public function get_by_id(int $id)
    {
        $query = "SELECT * FROM $this->table WHERE id = $id";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function get_by_nomor_bukti(int $nomor_bukti)
    {
        $query = "SELECT * FROM $this->table WHERE nomor_bukti = $nomor_bukti";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`nomor_bukti`,`kode_anggota`,`tanggal_pinjam`,`tanggal_kembali`,`kode_buku`) VALUES ('$this->nomor_bukti','$this->kode_anggota','$this->tanggal_pinjam','$this->tanggal_kembali','$this->kode_buku')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET nomor_bukti = '$this->nomor_bukti', kode_anggota = '$this->kode_anggota', tanggal_pinjam = '$this->tanggal_pinjam', tanggal_kembali = '$this->tanggal_kembali', kode_buku = '$this->kode_buku'
        WHERE idpinjam = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_nomor_bukti($nomor_bukti): int
    {
        $query = "UPDATE $this->table SET nomor_bukti = '$this->nomor_bukti', kode_anggota = '$this->kode_anggota', tanggal_pinjam = '$this->tanggal_pinjam', tanggal_kembali = '$this->tanggal_kembali', kode_buku = '$this->kode_buku'
        WHERE nomor_bukti = $nomor_bukti";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE idpinjam = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_nomor_bukti($nomor_bukti): int
    {
        $query = "DELETE FROM $this->table WHERE nomor_bukti = $nomor_bukti";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>