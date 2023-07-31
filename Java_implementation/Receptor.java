import java.util.ArrayList;

public class Receptor {

    View view = new View();

    ArrayList<Boolean> trama;
    ArrayList<Boolean> result;

    ArrayList<Boolean> polinomio;

    public Receptor(ArrayList<Boolean> trama) {

        this.trama = trama;

        // generate polinomio
        polinomio = new ArrayList<>();
        Boolean[] pol = {
            true, false, true, true, false, true, false, true, 
            false, false, false, true, false, true, false, true,
            false, false, false, false, true, true, true, false, 
            true, false, false, true, true, false, true, false
        };
        for (boolean b: pol) polinomio.add(b);

        CRC();

    }

    private void CRC() {

        ArrayList<Boolean> actual = new ArrayList<>();

        int EOL = polinomio.size();

        // initialize by coping the first 32 values
        for (int i = 0; i < polinomio.size() ;  i ++) {
            actual.add(trama.get(i));
        }

        while (EOL < trama.size()) {
            ArrayList<Boolean> temp = new ArrayList<>();

            System.out.println("\n");
            view.printTrama(actual);
            view.printTrama(polinomio);

            for (int i = 0; i < polinomio.size(); i ++) {
                temp.add(actual.get(i) ^ polinomio.get(i));
            }

            view.printTrama(temp);

            while (!temp.get(0) && EOL < trama.size()) {
                temp.add(trama.get(EOL));
                EOL ++;

                temp.remove(0); 
            }

            // replace actual for temporal
            actual = new ArrayList<>(temp);

        }

        System.out.println("\nResultado de receptor");
        view.printTrama(actual);
        actual.remove(0); // remove the first 0
        view.printTrama(actual);


    }

    
}
