package bot.cortex;

import android.app.Activity;
import android.util.Log;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.content.Intent;
import android.view.View;
import android.widget.TextView;
import android.widget.Button;
import android.app.ProgressDialog;

public class BookScanner extends Activity implements Runnable{
  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    
    Button nextScan = (Button) findViewById(R.id.next);
    startScanner(nextScan);
  }
  
  public BookInfo books = new BookInfo();
  
  public void onActivityResult(int requestCode, int resultCode, Intent intent) {
    if (requestCode == 0) {
      if (resultCode == RESULT_OK) {
        String contents = intent.getStringExtra("SCAN_RESULT");
        String format = intent.getStringExtra("SCAN_RESULT_FORMAT");
        
        books.setAccession(contents);
        loading = ProgressDialog.show(BookScanner.this, "", "Getting Book Info", true, false);
        thread.start();
      } 
    }
  }
  
  private Thread thread = new Thread(this);
  private ProgressDialog loading;
  private Handler msg = new Handler() {
    @Override
    public void handleMessage(Message message) {
      loading.dismiss();
      displayBarcode();
    }
  };
  
  public void run() {
    books.getShelfNumber();
    msg.sendEmptyMessage(0);
  }
  
  private void displayBarcode() {
    setContentView(R.layout.scanner);
    TextView tv = (TextView) findViewById(R.id.barcode);
    tv.setText(books.accession + "\n" + books.shelfNumber);
  }
    
  public void startScanner(View v) {
    Intent intent = new Intent("com.google.zxing.client.android.SCAN");
    intent.setPackage("com.google.zxing.client.android");
    intent.putExtra("SCAN_MODE", "ONE_D_MODE");
    startActivityForResult(intent, 0);
  }
  
  public void exitScan(View v) {
    finish();
  }
  
}


