package bot.cortex;

import java.net.*;
import java.io.*;
import android.util.Log;

public class BookInfo {
  public String accession;
  public String shelfNumber;
  
  public void getShelfNumber() {
    try {
      String data = URLEncoder.encode("T1", "UTF-8") + "=" + URLEncoder.encode(accession, "UTF-8");
      data += "&" + URLEncoder.encode("m_field", "UTF-8") + "=" + URLEncoder.encode("acc_no", "UTF-8");
      data += "&" + URLEncoder.encode("m_match", "UTF-8") + "=" + URLEncoder.encode("Words", "UTF-8");
      data += "&" + URLEncoder.encode("m_media", "UTF-8") + "=" + URLEncoder.encode("1", "UTF-8");
          
      URL lib = new URL("http://www.library.iitb.ac.in/newsearchbook/q_string.php");
      URLConnection conn = lib.openConnection();
      conn.setDoOutput(true);
      OutputStreamWriter writeURL = new OutputStreamWriter(conn.getOutputStream());
      writeURL.write(data);
      writeURL.flush();
          
      Log.d("Scanner", lib.toString() + "?" + data);
          
      BufferedReader result = new BufferedReader(new InputStreamReader(conn.getInputStream()));
      StringBuilder buff = new StringBuilder();
      String line = null;
      while ((line = result.readLine()) != null) {
        buff.append(line + "\n");
      }
      writeURL.close();
      result.close();
         
      String html = buff.toString();
      int ShelfStart = html.indexOf("<font color='blue'>");
      shelfNumber = html.substring(1 + html.indexOf(">", ShelfStart), html.indexOf("</font>", ShelfStart));
    }
    catch(Exception e) {
    }
  }
  
  public void setAccession(String acc) {
    accession = acc;
  }
}
