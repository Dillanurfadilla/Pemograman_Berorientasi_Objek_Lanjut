<?php
require_once 'database.php';
require_once 'Anggota.php';
$db = new MySQLDatabase();
$anggota = new Anggota($db);
$id=0;
$kode_anggota=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode_anggota'])){
            $kode_anggota = $_GET['kode_anggota'];
        }
        if($id>0){    
            $result = $anggota->get_by_id($id);
        }elseif($kode_anggota>0){
            $result = $anggota->get_by_kode_anggota($kode_anggota);
        } else {
            $result = $anggota->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new anggota
        $anggota->kode_anggota = $_POST['kode_anggota'];
        $anggota->nama = $_POST['nama'];
        $anggota->jk = $_POST['jk'];
        $anggota->prodi = $_POST['prodi'];
        $anggota->Alamat = $_POST['nlamat'];
       
        $anggota->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Anggota created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Anggota not created.';
        }
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'PUT':
        // Update an existing data
        $_PUT = [];
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode_anggota'])){
            $kode_anggota = $_GET['kode_anggota'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $anggota->kode_anggota = $_PUT['kode_anggota'];
        $anggota->nama = $_PUT['nama'];
        $anggota->jk = $_PUT['jk'];
        $anggota->prodi = $_PUT['prodi'];
        $anggota->Alamat = $_PUT['Alamat'];
        if($id>0){    
            $anggota->update($id);
        }elseif($kode_anggota<>""){
            $anggota->update_by_kode_anggota($kode_anggota);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Anggota updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Anggota update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['kode_anggota'])){
            $kode_anggota = $_GET['kode_anggota'];
        }
        if($id>0){    
            $anggota->delete($id);
        }elseif($kode_anggota>0){
            $anggota->delete_by_kode_anggota($kode_anggota);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Anggota deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Anggota delete failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    default:
        header("HTTP/1.0 405 Method Not Allowed");
        break;
    }
$db->close()
?>