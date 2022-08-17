public class Second {
    public static void main(String[] args) {
        // IF
        var numeroIf = -1;
        if (numeroIf > 0) {
            System.out.println("IF | El número es positivo");
        } else if (numeroIf == 0) {
            System.out.println("IF | El número es cero");
        }
        else {
            System.out.println("IF | El número es negativo");
        }
        //While
        var numeroWhile = 0;
        while (numeroWhile < 3) {
            System.out.println("WHILE | El número es: "+numeroWhile);
            numeroWhile++;
        }
        //Do While
        var numeroDoWhile = 0;
        do {
            System.out.println("DO WHILE | El número es: "+numeroDoWhile);
            numeroDoWhile++;
        }
        while (numeroDoWhile == 0);
        //For
        for (int numeroFor = 0; numeroFor <= 3; numeroFor++) {
            System.out.println("FOR | El número es: "+numeroFor);
        }
        //Switch
        var estacion = "Verano";

        switch (estacion) {
            case "Invierno":
                System.out.println("SWITCH | La estación es: "+estacion);
                break;
            case "Primavera":
                System.out.println("SWITCH | La estación es: "+estacion);
                break;
            case "Otoño":
                System.out.println("SWITCH | La estación es: "+estacion);
                break;
            case "Verano":
                System.out.println("SWITCH | La estación es: "+estacion);
                break;
            default:
                System.out.println("SWITCH | Este valor: "+estacion+"... no es una estación");
        }
    }
}
