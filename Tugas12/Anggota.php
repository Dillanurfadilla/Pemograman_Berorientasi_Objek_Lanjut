<?php
//Simpanlah dengan nama file : Anggota.php
require_once 'database.php';
class Anggota 
{
    private $db;
    private $table = 'anggota';
    public $kode_anggota = "";
    public $nama = "";
    public $jk = "";
    public $prodi = "";
    public $Alamat = "";
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
    public function get_by_kode_anggota(int $kode_anggota)
    {
        $query = "SELECT * FROM $this->table WHERE kode_anggota = $kode_anggota";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kode_anggota`,`nama`,`jk`,`prodi`,`Alamat`) VALUES ('$this->kode_anggota','$this->nama','$this->jk','$this->prodi','$this->Alamat')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kode_anggota = '$this->kode_anggota', nama = '$this->nama', jk = '$this->jk', prodi = '$this->prodi', Alamat = '$this->Alamat' 
        WHERE idanggota = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kode_anggota($kode_anggota): int
    {
        $query = "UPDATE $this->table SET kode_anggota = '$this->kode_anggota', nama = '$this->nama', jk = '$this->jk', prodi = '$this->prodi', Alamat = '$this->Alamat' 
        WHERE kode_anggota = $kode_anggota";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE idanggota = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_kode_anggota($kode_anggota): int
    {
        $query = "DELETE FROM $this->table WHERE kode_anggota = $kode_anggota";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>