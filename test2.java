
import java.util.ArrayList;
import java.util.List;

public class Test {
    public static void main(String[] args) {
        List<Employe> employes = new ArrayList<>();

        employes.add(new Vacataire("ALI", 200, 3.9f));
        employes.add(new Contractuel("Salah", 900));
        employes.add(new Permatent("Mohamed", 1100, 150));

        System.out.println("Descriptions des employés (avant modification) :");
        for (Employe employe : employes) {
            System.out.println(employe);
        }

        for (Employe employe : employes) {
            if (employe instanceof Vacataire) {
                ((Vacataire) employe).setPrixHeure(4.1f);
            }

            if (employe instanceof Permatent) {
                ((Permatent) employe).setPrime(230);
            }

            if (employe instanceof Contractuel) {
                ((Contractuel) employe).setSalaireBase(1000);
            }
        }


        System.out.println("\nDescriptions des employés (après modification) :");
        for (Employe employe : employes) {
            System.out.println(employe);
        }
    }
}
