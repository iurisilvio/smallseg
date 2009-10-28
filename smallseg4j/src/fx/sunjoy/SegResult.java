package fx.sunjoy;

import java.util.List;

public class SegResult{
	public List<String> recognised;
	
	public List<String> unrecognised;
	
	public String toString(){
		return "r:"+recognised+"\r\nu:"+unrecognised;
	}
}
