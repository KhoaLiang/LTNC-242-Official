import static util.Utility.isFibonacci;
import static util.Utility.whichPositionOfFibonacci;

public class Paladin extends Knight {
	public Paladin(int baseHp, int wp) {
		super(baseHp, wp);
	}

	@Override
	public double getCombatScore() {
		if(isFibonacci(getBaseHp()) == true && whichPositionOfFibonacci(getBaseHp()) > 2){
			return 1000 + whichPositionOfFibonacci(getBaseHp());
		}
		return getBaseHp() * 3;
	}
}
