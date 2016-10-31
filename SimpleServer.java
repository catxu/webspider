import java.net.*;
import java.io.*;

public	class SimpleServer {
	public static void main(String args[]) throws Exception {
		ServerSocket server = new ServerSocket(6127);
		Socket socket = server.accept();

		FileInputStream in = new FileInputStream("c://web//index.html");
		OutputStream out = socket.getOutputStream();

		int len = 0;
		byte buff[] = new byte[1024];
		while((len = in.read(buff)) > 0) {
			out.write(buff, 0, len);
		}

		in.close();
		out.close();
		socket.close();
		server.close();
	}
}