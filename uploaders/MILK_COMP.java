import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.sql.*;
import java.text.DecimalFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;

public class MILK_COMP {
    static final String DB_URL = "";
    static final String USER = "";
    static final String PASS = "";
    private static DecimalFormat format = new DecimalFormat("#.#");
    private static ArrayList<String> data = new ArrayList<>();


    private static final String DAMHEAD = "EAR_TAG,LACT_NO,SAMPLED_DATE,FEED_GROUP,YIELD_1,FAT_PERC_1,PROTEIN_PERC_1,CELL_COUNT_1,YIELD_2,FAT_PERC_2,PROTEIN_PERC_2,CELL_COUNT_2,YIELD_3,FAT_PERC_3,PROTEIN_PERC_3,CELL_COUNT_3,SAMPLED_DATE_MON,SAMPLED_DATE_TUE,SAMPLED_DATE_WED,SAMPLED_DATE_THU,SAMPLED_DATE_FRI,STDYIELD,AVGYIELD,STDFATPERC,AVGFATPERC,STDPROTEINPERC,AVGPROTEINPERC,STDCELLCOUNT,AVGCELLCOUNT";


    public static void main(String[] args) {
        readfile("cleanData/MILK_COMP.csv", DAMHEAD);
        System.out.println(data);
        // Open a connection
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conn = DriverManager.getConnection(DB_URL, USER, PASS);
            System.out.println("Connected to DB...");

            insertData(conn);
        } catch (Exception e) {
            e.printStackTrace();
       }
    }

    /**
     * Reads in the file and stores it into a static array of Data.
     * @param writefilename
     * @throws SQLException
     */
    private static void readfile(String writefilename, String validator) {
        BufferedReader reader = null;
        try {
            reader = new BufferedReader(new FileReader(writefilename));
            String line = "";
            // Reads the first line.
            line = reader.readLine();
            // Checks to see if the file is empty, if it is, terminates the program.
            // If the file is not empty, it checks to see if it is in the correct format to be processed, if it is not, then the program terminates.
            //if (!line.equals(validator)) {
                //System.out.println("This file is not in the correct format to be used.");
                //System.out.println("First line is " + line);
                //System.exit(0);
            //}
            // Reads the file and stores the data in a static ArrayList to put the values into the program.
            while ((line = reader.readLine()) != null) {
                data.add(line);
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found: " + e.getMessage());
            System.exit(0);
        } catch (IOException e) {
            System.out.println("IO Exception: " + e.getMessage());
            System.exit(0);
        } finally {
            if (reader != null) {
                try {
                    reader.close();
                } catch (IOException e) {
                    System.out.println("Couldn't close reader: " + e.getMessage());
                    System.exit(0);
                }
            }
        }
    }

    /**
     * Inserts the Data into the table using a batch statement.
     * @param connection
     * @throws SQLException
     */
    private static void insertData(Connection connection) throws SQLException {
        // Creates a prepared statement to insert the data.
        PreparedStatement statement = connection.prepareStatement("INSERT INTO " + "milk_comp" + " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)");
        // Goes through all of the data and inserts it into the prepared statement in a batch.
        for (int x = 0; x < data.size(); x++) {
            String[] elements = data.get(x).split(",");

            int earTag = Integer.parseInt(elements[0]);
            int LACT_NO = Integer.parseInt(elements[1]);
            String SAMPLED_DATE =(elements[2]);
            int Feed_GROUP = Integer.parseInt(elements[3]);
            double Yield1 = -1.0;
            System.out.println(elements[3]);
            if (!elements[4].equals("NULL")) {
                Yield1 = Double.parseDouble(elements[4]);
            }
            double FAT_PERC_1 = -1.0;
            if (!elements[5].equals("NULL")) {
                FAT_PERC_1 = Double.parseDouble(elements[5]);
            }
            double PROTEIN_PERC_1 = -1.0;
            if (!elements[6].equals("NULL")) {
                PROTEIN_PERC_1 = Double.parseDouble(elements[6]);
            }
            int CELL_COUNT_1 = -1;
            if (!elements[7].equals("NULL")) {
                CELL_COUNT_1 = Integer.parseInt(elements[7]);
            }
            double Yield2 = -1.0;
            if (!elements[8].equals("NULL")) {
                Yield2 = Double.parseDouble(elements[8]);
            }
            double FAT_PERC_2 = -1.0;
            if (!elements[9].equals("NULL")) {
                FAT_PERC_2 = Double.parseDouble(elements[9]);
            }
            double PROTEIN_PERC_2 = -1.0;
            if (!elements[10].equals("NULL")) {
                PROTEIN_PERC_2 = Double.parseDouble(elements[10]);
            }
            int CELL_COUNT_2 = -1;
            if (!elements[11].equals("NULL")) {
                CELL_COUNT_2 = Integer.parseInt(elements[11]);
            }
            double Yield3 = -1.0;
            if (!elements[12].equals("NULL")) {
                Yield3 = Double.parseDouble(elements[12]);
            }
            double FAT_PERC_3 = -1.0;
            if (!elements[13].equals("NULL")) {
                FAT_PERC_3 = Double.parseDouble(elements[13]);
            }
            double PROTEIN_PERC_3 = -1.0;
            if (!elements[14].equals("NULL")) {
                PROTEIN_PERC_3 = Double.parseDouble(elements[14]);
            }
            int CELL_COUNT_3 = -1;
            if (!elements[15].equals("NULL")) {
                CELL_COUNT_3 = Integer.parseInt(elements[15]);
            }
            String SAMPLED_DATE_MON =(elements[16]);
            String SAMPLED_DATE_TUE =(elements[17]);
            String SAMPLED_DATE_WED =(elements[18]);
            String SAMPLED_DATE_THU =(elements[19]);
            String SAMPLED_DATE_FRI =(elements[20]);

            double STDYIELD = Double.parseDouble(elements[21]);
            double AVGYIELD = Double.parseDouble(elements[22]);
            double STDFATPERC = Double.parseDouble(elements[23]);
            double AVGFATPERC = Double.parseDouble(elements[24]);
            double STDPROTEINPERC = Double.parseDouble(elements[25]);
            double AVGPROTEINPERC = Double.parseDouble(elements[26]);
            double STDCELLCOUNT = Double.parseDouble(elements[27]);
            double AVGCELLCOUNT = Double.parseDouble(elements[28]);



            statement.setInt(1, earTag);
            statement.setInt(2, LACT_NO);
            statement.setString(3, SAMPLED_DATE);
            statement.setInt(4, Feed_GROUP);
            if (Yield1 < 0.0) {
                System.out.println("Here");
                statement.setNull(5, Types.DOUBLE);
            } else {
                statement.setDouble(5, Yield1);

            }
            if (FAT_PERC_1 < 0.0) {
                System.out.println("Here");
                statement.setNull(6, Types.DOUBLE);
            } else {
                statement.setDouble(6, FAT_PERC_1);

            }
            if (PROTEIN_PERC_1 < 0.0) {
                System.out.println("Here");
                statement.setNull(7, Types.DOUBLE);
            } else {
                statement.setDouble(7, PROTEIN_PERC_1);

            }
            if (CELL_COUNT_1 < 0) {
                System.out.println("Here");
                statement.setNull(8, Types.DOUBLE);
            } else {
                statement.setInt(8, CELL_COUNT_1);

            }
            if (Yield2 < 0.0) {
                System.out.println("Here");
                statement.setNull(9, Types.DOUBLE);
            } else {
                statement.setDouble(9, Yield2);

            }
            if (FAT_PERC_2 < 0.0) {
                System.out.println("Here");
                statement.setNull(10, Types.DOUBLE);
            } else {
                statement.setDouble(10, FAT_PERC_2);

            }
            if (PROTEIN_PERC_2 < 0.0) {
                System.out.println("Here");
                statement.setNull(11, Types.DOUBLE);
            } else {
                statement.setDouble(11, PROTEIN_PERC_2);

            }
            if (CELL_COUNT_2 < 0) {
                System.out.println("Here");
                statement.setNull(12, Types.DOUBLE);
            } else {
                statement.setInt(12, CELL_COUNT_2);

            }
            if (Yield3 < 0.0) {
                System.out.println("Here");
                statement.setNull(13, Types.DOUBLE);
            } else {
                statement.setDouble(13, Yield3);

            }
            if (FAT_PERC_3 < 0.0) {
                System.out.println("Here");
                statement.setNull(14, Types.DOUBLE);
            } else {
                statement.setDouble(14, FAT_PERC_3);

            }
            if (PROTEIN_PERC_3 < 0.0) {
                System.out.println("Here");
                statement.setNull(15, Types.DOUBLE);
            } else {
                statement.setDouble(15, PROTEIN_PERC_3);

            }
            if (CELL_COUNT_3 < 0) {
                System.out.println("Here");
                statement.setNull(16, Types.DOUBLE);
            } else {
                statement.setInt(16, CELL_COUNT_3);

            }
            statement.setString(17, SAMPLED_DATE_MON);
            statement.setString(18, SAMPLED_DATE_TUE);
            statement.setString(19, SAMPLED_DATE_WED);
            statement.setString(20, SAMPLED_DATE_THU);
            statement.setString(21, SAMPLED_DATE_FRI);
            statement.setDouble(22, STDYIELD);
            statement.setDouble(23, AVGYIELD);
            statement.setDouble(24, STDFATPERC);
            statement.setDouble(25, AVGFATPERC);
            statement.setDouble(26, STDPROTEINPERC);
            statement.setDouble(27, AVGPROTEINPERC);
            statement.setDouble(28, STDCELLCOUNT);
            statement.setDouble(29, AVGCELLCOUNT);
            // A batch is used in order to execute all of the inserts at once.

            statement.addBatch();
        }
        // Inserts all of the data at once, commits the data in order to validate the inputs manually.

        System.out.println("hello");
        statement.executeBatch();
        System.out.println("hello");
        //connection.commit();
        statement.close();
    }


    /**
     * Checks to see if a String variable can be parsed as a double.
     * @param tocheck
     * @return
     */
    private static boolean checkDouble(String tocheck) {
        try {
            Double.parseDouble(tocheck);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }

    /**
     * Prints resuolts for a query
     * @param resultSet
     * @throws SQLException
     */

}
