package fx.sunjoy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;
import java.util.regex.Matcher;
import java.util.regex.Pattern;



public class Seg {
	private Map<Character, Map> d = new TreeMap<Character, Map>();
	private Set<Character> stopWords = new HashSet<Character>();
	
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
			is.close();
			is = Thread.currentThread().getContextClassLoader().getResourceAsStream("fx/sunjoy/dic/suffix.dic");
			reader = new BufferedReader(new InputStreamReader(is,"utf-8"));
			words = new ArrayList<String>();
			while(true){
				String word = reader.readLine();
				if(word==null || word.equals(""))
					break;
				stopWords.add(word.charAt(0));
			}
			
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
			word = (char)11+word;
			p = d;
			for(int i=word.length()-1;i>=0;i--){
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
	
	private List<String> _binary_seg(String s){
		int ln = s.length();
		List<String> R = new ArrayList<String>();
		if(ln==1){
			R.add(s);
			return R;
		}
		for(int i=ln;i>1;i--){
			String tmp = s.substring(i-2,i);
			if(stopWords.contains(tmp.charAt(0))){
				R.add(tmp.substring(1,2));
				R.add(tmp.substring(0,1));
			}
			else
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
		Splitter spliter = new Splitter("([0-9A-Za-z\\-\\+#@_\\.]+)",true);
		for(int i=tmp.length-1;i>-1;i--){
			String[] mc = spliter.split(tmp[i]);
			for(int j=mc.length-1;j>-1;j--){
				String r = mc[j];
				if(Pattern.matches("([0-9A-Za-z\\-\\+#@_\\.]+)", r))
					R.add(r);
				else
					R.addAll(_binary_seg(r));
			}
		}
		return R;
	}
	
	public List<String> cut(String text){
		Map<Character,Map> p = d;
		int ln = text.length();
		int i=ln;
		int j=0;
		int z=ln;
		List<String> recognised = new ArrayList<String>();
		Integer[] mem = null;
		while(i-j>0){
			Character t = Character.toLowerCase(text.charAt(i-1-j));
			if(!p.containsKey(t)){
				if(mem!=null){
					i = mem[0];j=mem[1];z=mem[2];
					p = d;
					if(i<ln && i<z)
						recognised.addAll(_pro_unreg(text.substring(i,z)));
					recognised.add(text.substring(i-j,i));
					i = i-j;
					z = i;
					j = 0;
					mem = null;
					continue;
				}
				j = 0;
				i--;
				p = d;
				continue;
			}
			p = p.get(t);
			j++;
			if(p.containsKey((char)11)){
				if(j<=2){
					mem = new Integer[]{i,j,z};
					Character xsuffix = text.charAt(i-1);
					if(stopWords.contains(xsuffix)){
						p = d;
						i--;
						j=0;
					}
					continue;
				}
				p = d;
				if(i<ln && i<z)
					recognised.addAll(_pro_unreg(text.substring(i,z)));
				recognised.add(text.substring(i-j,i));
				i = i-j;
				z = i;
				j = 0;
				mem = null;
			}
		}
		if(mem!=null){
			i = mem[0];j=mem[1];z=mem[2];
			recognised.addAll(_pro_unreg(text.substring(i,z)));
			recognised.add(text.substring(i-j,i));
		}
		else
			recognised.addAll(_pro_unreg(text.substring(i-j,z)));
		
		return recognised;
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
		System.out.println(seg.cut("abc lxx adf我爱北京"));
	}
}
