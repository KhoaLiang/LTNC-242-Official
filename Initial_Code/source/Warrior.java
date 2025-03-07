import util.Utility;
public class Warrior extends Fighter {
    public Warrior(int baseHp, int wp) {
        super(baseHp, wp);
    }

    @Override
    public double getCombatScore() {
        if(isPrime(GROUND) == true){
            return getBaseHp() * 2;
        }
        if(getWp() == 1.0){
            return getBaseHp();
        }
        return getBaseHp() / 10;
    }
}
