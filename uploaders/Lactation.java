import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.sql.*;
import java.text.DecimalFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;

public class Lactation {
    static final String DB_URL = "";
    static final String USER = "";
    static final String PASS = "";
    private static DecimalFormat format = new DecimalFormat("#.#");
    private static ArrayList<String> data = new ArrayList<>();


    private static final String DAMHEAD = "EAR_TAG,LACT_NO,RECORD_TYPE,CALVING_DATE,CALVING_WGT,CALVING_COND_SCORE,CALVING_EASE,NO_OF_CALVES,NO_OF_CALVES_DEAD,LACT_START_DATE,DRYING_DATE,DRYING_WGT,DRYING_COND_SCORE,DOB,RECORDER";


    public static void main(String[] args) {
        readfile("cleanData/LACTATION.csv", DAMHEAD);
        System.out.println(data);
        // Open a connection
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conn = DriverManager.getConnection(DB_URL, USER, PASS);
            System.out.println("Connected to DB...");

            insertData(conn);


            //Statement stmt = conn.createStatement();
            //String test = "INSERT INTO dam VALUES (1, 1, 1, 1, 1, 1, 1, 1, 1, 11/11/11, 1, 1)";
            //stmt.executeUpdate(test);

            //stmt = conn.createStatement();
            //String sql = "SELECT * from langhillherd.dam";
            //ResultSet set = stmt.executeQuery(sql);
            //printResults(set);
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
        PreparedStatement statement = connection.prepareStatement("INSERT INTO " + "lactation" + " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)");
        // Goes through all of the data and inserts it into the prepared statement in a batch.
        for (int x = 0; x < data.size(); x++) {
            String[] elements = data.get(x).split(",");

            int earTag = Integer.parseInt(elements[0]);
            int LACT_NO = Integer.parseInt(elements[1]);
            String RECORD_TYPE = (elements[2]);
            String CALVING_DATE = (elements[3]);
            int CALVING_WGT = -1;
            if (!elements[4].equals("NULL")) {
                CALVING_WGT = Integer.parseInt(elements[4]);
            }
            double CALVING_COND_SCORE = -1.0;
            System.out.println(elements[5]);
            if (!elements[5].equals("NULL")) {
                CALVING_COND_SCORE = Double.parseDouble(elements[5]);
            }


            String CALVING_EASE = (elements[6]);
            int NO_OF_CALVES = Integer.parseInt(elements[7]);
            int NO_OF_CALVES_DEAD = Integer.parseInt(elements[8]);
            String LACT_START_DATE = (elements[9]);
            String DRYING_DATE = (elements[10]);
            int DRYING_WGT = -1;
            if (!elements[11].equals("NULL")) {
                DRYING_WGT = Integer.parseInt(elements[11]);
            }
            double DRYING_COND_SCORE = -1.0;
            if (!elements[12].equals("NULL")) {
                DRYING_COND_SCORE = Double.parseDouble(elements[12]);
            }
            String DOB = (elements[13]);
            int RECORDER = Integer.parseInt(elements[14]);

            statement.setInt(1, earTag);
            statement.setInt(2, LACT_NO);
            statement.setString(3, RECORD_TYPE);
            statement.setString(4, CALVING_DATE);
            if (CALVING_WGT < 0) {
                System.out.println("Here");
                statement.setNull(5, Types.DOUBLE);
            } else {
                statement.setInt(5, CALVING_WGT);
            }
            if (CALVING_COND_SCORE < 0.0) {
                System.out.println("Here");
                statement.setNull(6, Types.DOUBLE);
            } else {
                statement.setDouble(6, CALVING_COND_SCORE);
            }

            statement.setString(7, CALVING_EASE);
            statement.setInt(8, NO_OF_CALVES);
            statement.setInt(9, NO_OF_CALVES_DEAD);
            statement.setString(10, LACT_START_DATE);
            statement.setString(11, DRYING_DATE);
            if (DRYING_WGT < 0) {
                System.out.println("Here");
                statement.setNull(12, Types.DOUBLE);
            } else {
                statement.setInt(12, DRYING_WGT);
            }
            if (DRYING_COND_SCORE < 0.0) {
                System.out.println("Here");
                statement.setNull(13, Types.DOUBLE);
            } else {
                statement.setDouble(13, DRYING_COND_SCORE);
            }
            statement.setString(14, DOB);
            statement.setInt(15,RECORDER);
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


}
