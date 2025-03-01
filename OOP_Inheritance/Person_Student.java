class Person{
	private String name;
	private int dob;
	public Person(String name, int dob) {
		this.name = name;
		this.dob = dob;
	}
	public String getName(){
        return name;
    }
    public int getDob(){
        return dob;
    }
}

class Student extends Person {
    private double GPA;
	public Student(String name, int dob, double GPA){
        super(name, dob);
        this.GPA = GPA;
    }
    public double getGpa(){
        return GPA;
    }
}

public class Person_Student {
	public static void main(String[] args) {
		Student s = new Student("Hai", 2002, 8.8);
		System.out.println("Name: " + s.getName());
		System.out.println("Date of birth: " + s.getDob());
		System.out.println("GPA: " + s.getGpa());
	}
}