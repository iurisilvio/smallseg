package fx.sunjoy;

import java.util.ArrayList;
import java.util.List;

public class SmallSeg {
	private static Seg seg = new Seg();
	static{
		seg.useDefaultDict();
	}
	public static List<String> cut(String text){
		List<String> result = new ArrayList<String>();
		SegResult sr = seg.cut(text);
		result.addAll(sr.recognised);
		result.addAll(sr.unrecognised);
		return result;
	}
}
