import javax.sound.midi.SysexMessage;

public class Main {
    public static void main (String[] args){

        //Person object
        Persona persona = new Persona();
        persona.setEdad(35);
        persona.setNombre("Giuliano De Leonardis");
        persona.setTelefono("+584141123880");
        System.out.println("La persona de nombre: "+persona.getNombre()+"\nTiene una edad de: "+persona.getEdad()+" años.\nSu número de teléfono es: "+persona.getTelefono());

    }
}

class Persona {
    private int edad;
    private String nombre;
    private String telefono;

    //Set and Get for "edad"
    public void setEdad(int edad) {
        this.edad = edad;
    }
    public int  getEdad() {
        return this.edad;
    }
    //Set and Get for "nombre"
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String  getNombre() {
        return this.nombre;
    }
    //Set and Get for "telefono"
    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }
    public String  getTelefono() {
        return this.telefono;
    }
}
