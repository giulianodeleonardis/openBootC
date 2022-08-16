public class Main {
    public static void main (String[] args){
        //Suma de dos
        int sumTwo = suma(20, 30);
        System.out.println("Suma de dos: "+sumTwo);
        //Suma de tres
        int sumThree = tripleSum(10, 20, 30);
        System.out.println("Suma de tres: "+sumThree);
        //Coche
        Coche miCoche = new Coche();
        miCoche.SumPuertas();
        System.out.println("El coche tiene "+miCoche.puertas+" puerta(s)");
        //Potato
        Potato miPotato = new Potato();
        miPotato.QuitarBrazos();
        System.out.println("Potato tiene "+miPotato.brazos+" brazo(s)");
    }
    public static int suma (int a, int b){
        return (a + b);
    }
    public static int tripleSum (int a, int b, int c) {
        return (a + b + c);
    }
}
class Potato {
    public int brazos= 0;
    public void QuitarBrazos(){
        this.brazos--;
    }
}
class Coche {
    public int puertas = 0;
    public void SumPuertas(){
        this.puertas++;
    }
}

