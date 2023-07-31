import java.util.ArrayList;
import java.util.Random;

public class Emisor {

    Random rand = new Random();
    View view = new View();

    ArrayList<Boolean> trama = new ArrayList<>();
    ArrayList<Boolean> tramaOriginal;
    ArrayList<Boolean> polinomio;
    ArrayList<Boolean> result;

    public Emisor(String input) {

        for (char c: input.toCharArray()) {
            if (c == '1') {
                trama.add(true);
            }
            else if (c == '0') trama.add(false);
        }

        // save a copy of the original before padding
        tramaOriginal = new ArrayList<>(trama);

        // Padding
        // while (trama.size() % 32 != 0 ) {
            for ( int i = 0; i < 31; i ++  ) {
                trama.add(false);
            }

        System.out.println("\ncon padding");
        view.printTrama(trama);

        // generate polinomio
        polinomio = new ArrayList<>();
        // polinomio.add(true); // The fist has to be 1
        // for (int i = 0; i < 32; i ++ ){
        //     polinomio.add(rand.nextBoolean());
        // }
        Boolean[] pol = {
            true, false, true, true, false, true, false, true, 
            false, false, false, true, false, true, false, true,
            false, false, false, false, true, true, true, false, 
            true, false, false, true, true, false, true, false
        };
        for (boolean b: pol) polinomio.add(b);

        System.out.println("\npolinomio");
        view.printTrama(polinomio);

        // excecute algorithm
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

        System.out.println("\nactual");
        view.printTrama(actual);
        actual.remove(0); // remove the first 0
        view.printTrama(actual);

        // Add the result to the original trama
        result = new ArrayList<>(tramaOriginal);
        result.addAll(actual);

        System.out.println("\nResultado final");
        view.printTrama(result);

    }

    public ArrayList<Boolean> getPolinomio() {
        return polinomio;
    }

    public ArrayList<Boolean> get_response() {
        return result;
    }

    public boolean getParidad() {
        // Calculate paridad
        int cantOnes = 0;
        for (boolean b: trama) {
            if (b) cantOnes ++;
        }

        if (cantOnes % 2 == 0) return true;
        else return false;
    }
    
    
}
