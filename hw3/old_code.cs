using System;
using System.Collections.Generic;

abstract class Instructor
{
    public virtual string ScheduleTeachingLoad(int instructorId)
    {
        return "Teaching Load is Scheduled";
    }
    public virtual string BecomeDepartmentChairperson(int instructorId)
    {
        return "Great.  More work, more herding cats, and no more pay";
    }
}

class TeachingAssistant : Instructor
{
    public override string ScheduleTeachingLoad(int instructorId)
    {
        return "Teaching Load is Scheduled";
    }
    public override string BecomeDepartmentChairperson(int instructorId)
    {
        return "I can't be a Department Chairperson";
    }
}

class FullProfessor : Instructor
{
    public override string ScheduleTeachingLoad(int instructorId)
    {
        return "Teaching Load is Scheduled";
    }
    public override string BecomeDepartmentChairperson(int instructorId)
    {
        return "Damn.";
    }
}

class ContractualInstructor : Instructor
{
    public override string ScheduleTeachingLoad(int instructorId)
    {
        return "Teaching Load is Scheduled";
    }
}

public class HRManager
{
   static public void Main(string [] args)
   {
      Console.WriteLine("Well, at least you got mono working");
      List<Instructor> instructorList = new List<Instructor>();
		instructorList.Add(new FullProfessor());
      instructorList.Add(new ContractualInstructor());
      instructorList.Add(new TeachingAssistant());
      foreach (Instructor e in instructorList)
      {
          e.BecomeDepartmentChairperson(1245);
      }
   }
}
