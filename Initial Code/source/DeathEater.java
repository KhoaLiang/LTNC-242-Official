import util.Utility;
public class DeathEater extends Monster implements Combatable {
	public DeathEater(Complex mana) {
		super(mana);
	}

	@Override
	public double getCombatScore() {
		return Math.sqrt(getMana().getRe() * getMana().getRe() + getMana().getIm() * getMana().getIm());
	}
}
