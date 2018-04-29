using System;
using System.Linq;
using System.Collections.Generic;

namespace TroubleTrignometry
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            TroubleTrignometryMethod();
        }

        private static string TroubleTrignometryMethod()
        {
            int [] inputs = {3,10,3000000,2920383,1800228,901007};
            List<string> result = new List<string>();
            foreach(var input in inputs)
            {
                List<double> values = new List<double>();
                for(int x = 0;x<=input;x++)
                {
                    for(int y=0;y<=input;y++)
                    {
                        for(int z=0;z<=input;z++)
                        {
                            if((x+y+z)==input)
                            {
                                var res = Math.Sin(x)+Math.Sin(y)+Math.Sin(z);
                                values.Add(res);
                            }                    
                        }
                    }
                }
                var max_result = values.Max();
                var resultoutput = $"{input} -> {max_result}";
                result.Add(resultoutput);
                Console.WriteLine(resultoutput);
            }
            var resultStr = string.Join(",", result.ToArray());
            Console.WriteLine(resultStr);
            return resultStr;
        }
    }
}