import util.Utility;

public class Knight extends Fighter {
    public Knight(int baseHp, int wp) {
        super(baseHp, wp);
    }

    @Override
    public double getCombatScore() {
        if(isSquare(GROUND) == true){
            return getBaseHp() * 2;
        }
        if(getWp() == 1.0){
            return getBaseHp();
        }
        return getBaseHp() / 10;
    }
}
