
import EditRuleForm from "../../components/EditRuleForm";
import { Rule } from "../../../../types";
const getRuleById = async ({ id }: { id: Rule['id'] }) => {
  try {
    const res = await fetch(`http://localhost:3000/api/rules/${id}`, {
      cache: "no-store",
    });

    if (!res.ok) {
      throw new Error("Failed to fetch rules");
    }

    return res.json();
  } catch (error) {
    console.log(error);
  }
};

export default async function EditRule({ params }: { params: { id: number } }) {
  const { id } = params;
  const { rule } = await getRuleById({ id });
  const { example, description } = rule;

  return <EditRuleForm id={id} example={example} description={description} />;
}