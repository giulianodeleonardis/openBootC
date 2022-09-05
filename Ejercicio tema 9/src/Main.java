public class Main {
    public static void main(String[] args){
        //Cliente
        Cliente cliente = new Cliente();
        cliente.setEdad(25);
        cliente.setNombre("Giuliano");
        cliente.setTelefono("+5812345678945");
        cliente.credito = 1000;
        System.out.println("***CLIENTE***\n"+"Nombre del cliente: "+cliente.nombre+"\n"+"Edad del cliente: "+cliente.edad+"\n"+"Número de teléfono del cliente: "+cliente.telefono+"\n"+"Crédito del cliente: "+cliente.credito+"\n");
        //Trabajador
        Trabajador trabajador = new Trabajador();
        trabajador.setEdad(35);
        trabajador.setNombre("Julián");
        trabajador.setTelefono("+5998745612345");
        trabajador.salario = 700;
        System.out.println("***TRABAJADOR***\n"+"Nombre del trabajador: "+trabajador.nombre+"\n"+"Edad del trabajador: "+trabajador.edad+"\n"+"Número de teléfono del trabajador: "+trabajador.telefono+"\n"+"Salario del trabajador: "+trabajador.salario);
    }
}
class Persona {
    int edad;
    String nombre;
    String telefono;
}
//Cliente
class Cliente extends  Persona {
    int credito;
    //Edad
    public int getEdad() {
        return (this.edad);
    }
    public void setEdad(int edad) {
        this.edad = edad;
    }
    //Nombre
    public String getNombre() {
        return (this.nombre);
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    //Telefono
    public String getTelefono() {
        return (this.telefono);
    }
    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }
}
//Trabajador
class Trabajador extends  Persona {
    int salario;
    //Edad
    public int getEdad() {
        return (this.edad);
    }
    public void setEdad(int edad) {
        this.edad = edad;
    }
    //Nombre
    public String getNombre() {
        return (this.nombre);
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    //Telefono
    public String getTelefono() {
        return (this.telefono);
    }
    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }
}
