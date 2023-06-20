//Mahasiswa.php

public function get_row_all() 
{
    $query = "SELECT * FROM $this->table";
    $result_set = $this->db->query($query);
    return $this->db->affected_rows();
}

public function get_row_by_nim(int $nim)
{
    $query = "SELECT * FROM $this->table WHERE nim = $nim";
    $result_set = $this->db->query($query);   
    return $this->db->affected_rows();
}

//mahasiswa_api.php

case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['nim'])){
            $nim = $_GET['nim'];
        }
        if($id>0){    
            $result = $mahasiswa->get_by_id($id);
        }elseif($nim>0){
            $result = $mahasiswa->get_by_nim($nim);
            $rows = $mahasiswa->get_row_by_nim($nim);
        } else {
            $result = $mahasiswa->get_all();
            $rows = $mahasiswa->get_row_all();
        }        
        
        $val = array();
        if($rows==0){
            $val["status"]="failed";
            $val["message"]="Data is Empty";
        } else {
            
            while ($row = $result->fetch_assoc()) {    

                $val[] = $row;
            }
        }
        
        
        header('Content-Type: application/json');
        
        echo json_encode($val);
        break;