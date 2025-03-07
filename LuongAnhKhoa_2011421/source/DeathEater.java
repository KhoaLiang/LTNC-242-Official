
public class DeathEater extends Monster implements Combatable {
	public DeathEater(Complex mana) {
		super(mana);
	}

	@Override
	public double getCombatScore() {
		if (Math.sqrt(getMana().getRe() * getMana().getRe() + getMana().getIm() * getMana().getIm()) > 999) {
			return 999;
		}
		return Math.sqrt(getMana().getRe() * getMana().getRe() + getMana().getIm() * getMana().getIm());
	}
}
