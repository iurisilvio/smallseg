package fx.sunjoy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.util.regex.Matcher;
import java.util.regex.Pattern;



public class Seg {
	private Map<Character, Map> d = new TreeMap<Character, Map>();
	
	public void useDefaultDict(){
		try {
			InputStream is = Thread.currentThread().getContextClassLoader().getResourceAsStream("fx/sunjoy/dic/main.dic");
			BufferedReader reader = new BufferedReader(new InputStreamReader(is,"utf-8"));
			List<String> words = new ArrayList<String>();
			while(true){
				String word = reader.readLine();
				if(word==null || word.equals(""))
					break;
				words.add(word);
			}
			
			set(words);
		} catch (UnsupportedEncodingException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	public void set(List<String> words){
		Map<Character,Map> p = d;
		Map<Character,Map> q = null;
		Character k = null;
		for(String word: words){
			word += (char)11;
			p = d;
			for(int i=0;i<word.length();i++){
				Character cc = Character.toLowerCase(word.charAt(i));
				if(p == null){
					q.put(k, new TreeMap<Character,Object>());
					p = q.get(k);
				}
				if(!p.containsKey(cc)){
					p.put(cc, null);
					q = p;
					k = cc;
				}
				p = p.get(cc);
			}
			
		}
		
	}
	private List<String> _suffix_ary(String s){
		int ln = s.length();
		List<String> R = new ArrayList<String>();
		for(int i=0;i<ln;i++){
			String tmp = s.substring(i);
			if(tmp.length()>1)
				R.add(tmp);
		}
		return R;
	}
	private List<String> findAll(String pattern,String text){
		List<String> R = new ArrayList<String>();
		Matcher mc = Pattern.compile(pattern).matcher(text);
		while(mc.find()){
			R.add(mc.group(1));
		}
		return R;
	}
	private List<String> _pro_unreg(String piece){
		List<String> R = new ArrayList<String>();
		String[] tmp = piece.replaceAll("。|，|,|！|…|!|《|》|<|>|\"|'|:|：|？|\\?|、|\\||“|”|‘|’|；|—|（|）|·|\\(|\\)|　"," ").split("\\s");
		for(String ut : tmp){
			List<String> mc = findAll("([0-9A-Za-z\\-\\+#@_\\.]+)",ut);
			if(mc.size()>0){
				R.addAll(mc);
				String[] han =  ut.split("([0-9A-Za-z\\-\\+#@_\\.]+)");
				for(String h : han){
					R.addAll(_suffix_ary(h));
				}
			}else{
				R.addAll(_suffix_ary(ut));
			}
		}
		return R;
	}
	
	public SegResult cut(String text){
		Map<Character,Map> p = d;
		int i=0;
		int j=0;
		int z=0;
		List<String> recognised = new ArrayList<String>();
		List<String> unrecognised = new ArrayList<String>();
		int ln = text.length();
		while(i+j<ln){
			Character t = Character.toLowerCase(text.charAt(i+j));
			if(!p.containsKey(t)){
				j = 0;
				i++;
				p = d;
				continue;
			}
			p = p.get(t);
			j++;
			if(p.containsKey((char)11)){
				p = d;
				recognised.add(text.substring(i,i+j));
				unrecognised.addAll(_pro_unreg(text.substring(z,i)));
				i = i+j;
				z = i;
				j = 0;
			}
		}
		unrecognised.addAll(_pro_unreg(text.substring(z,i+j)));
		SegResult result = new SegResult();
		result.recognised = recognised;
		result.unrecognised = unrecognised;
		return result;
	}
	
	public static void main(String[] args) {
		Seg seg = new Seg();
		List<String> words = new ArrayList<String>();
		words.add("ab");
		words.add("abc");
		words.add("adf");
		words.add("北京");
		seg.set(words);
		System.out.println(seg.d);
		System.out.println(seg.cut("abcdefg love北京 adfxxx我爱你"));
	}
}
