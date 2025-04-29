public class chal {
    public static void main(String[] args) {
        String encodedFlag = "ZrgnPGS{pncchppvab_jvgu_n_ebgngvba_bs_pernz_cyrnfr}";
        
        if (args.length == 0) {
            System.out.println("Usage: java caffeine_conundrum.java <your_guess>");
            System.out.println("Hint: The barista left a flag, but it seems to be encoded...");
            return;
        }

        String userGuess = args[0];
        String encodedGuess = encodeFlag(userGuess);
        
        if (encodedGuess.equals(encodedFlag)) {
            System.out.println("Correct! Time for a coffee break!");
        } else {
            System.out.println("Not quite it! Keep trying...");
        }
    }

    // The barista's encoding method
    private static String encodeFlag(String input) {
        StringBuilder result = new StringBuilder();
        for (char c : input.toCharArray()) {
            if (Character.isLetter(c)) {
                // ROT13 transformation
                char base = Character.isUpperCase(c) ? 'A' : 'a';
                result.append((char) (base + (c - base + 13) % 26));
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}
