package fx.sunjoy;

public class Test {
	public static void main(String[] args) throws Exception {

		System.out.println(SmallSeg.cut("日照香炉生紫烟，遥看瀑布挂前川。飞流直下三千尺，疑是银河落九天。"));
		System.out.println(SmallSeg.cut("伊藤洋华堂总府店"));
		System.out.println(SmallSeg
				.cut("工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作"));
		System.out.println(SmallSeg.cut("我购买了道具和服装。草泥马"));
		System.out.println(SmallSeg.cut("我爱北京天安门"));
		System.out.println(SmallSeg.cut("中国科学院"));
		System.out.println(SmallSeg.cut("雷猴是个好网站"));
		System.out.println(SmallSeg.cut(("总经理完成了这件事情")));
		System.out.println(SmallSeg.cut(("电脑修好了")));
		System.out.println(SmallSeg.cut(("做好了这件事情就一了百了了")));
		System.out.println(SmallSeg.cut(("人们审美的观点是不同的")));
		System.out.println(SmallSeg.cut(("我们买了一个美的空调")));
		System.out.println(SmallSeg.cut(("中国的首都是北京")));
		System.out.println(SmallSeg.cut(("买水果然后来世博园")));
		System.out.println(SmallSeg.cut(("还需要很长的路要走")));
		System.out.println(SmallSeg.cut(("在过去的这五年")));
	}
}
